import socket

LISTEN_HOST = "localhost"
LISTEN_PORT = 8000
WINDOW_SIZE = 4

receiver = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
receiver.bind((LISTEN_HOST, LISTEN_PORT))

expected_seq = 0
buffer = {}

print("\n=== Selective Repeat Receiver Started ===")
print(f"Listening on {LISTEN_HOST}:{LISTEN_PORT} ...")
print(f"Receive window size: {WINDOW_SIZE}\n")

while True:
    raw_data, sender_address = receiver.recvfrom(1024)
    frame = raw_data.decode()
    seq_str, message = frame.split(":", 1)
    seq_num = int(seq_str)
    print("-" * 56)
    print(f"  Frame Received  -> seq={seq_num}  msg='{message}'")

    if seq_num == expected_seq:
        print(f"  In-order. Delivering: '{message}'")
        expected_seq += 1
        while expected_seq in buffer:
            buffered_msg = buffer.pop(expected_seq)
            print(f"  Flushing buffer -> seq={expected_seq}  msg='{buffered_msg}'  "
                  f"[was buffered, now delivering in order]")
            expected_seq += 1

        if buffer:
            print(f"  Buffer still holds: {sorted(buffer.keys())}")
        else:
            print(f"  Buffer is empty. Next expected seq={expected_seq}")

        ack = f"ACK{seq_num}"
        receiver.sendto(ack.encode(), sender_address)
        print(f"  ACK Sent        -> {ack}")

    elif expected_seq < seq_num < expected_seq + WINDOW_SIZE:
        if seq_num not in buffer:
            buffer[seq_num] = message
            print(f"  Out-of-order. BUFFERED seq={seq_num}  "
                  f"(waiting for seq={expected_seq} first)")
            print(f"  Buffer now holds: {sorted(buffer.keys())}")
        else:
            print(f"  Duplicate out-of-order frame seq={seq_num}. Already buffered.")

        ack = f"ACK{seq_num}"
        receiver.sendto(ack.encode(), sender_address)
        print(f"  ACK Sent        -> {ack}  (individual, out-of-order)")

    else:
        print(f"  Duplicate / outside window (seq={seq_num}, "
              f"expected={expected_seq}). Re-sending ACK.")
        ack = f"ACK{seq_num}"
        receiver.sendto(ack.encode(), sender_address)
        print(f"  ACK Sent        -> {ack}  (re-sent for duplicate)")
    print("-" * 56 + "\n")