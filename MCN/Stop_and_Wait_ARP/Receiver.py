import socket

LISTEN_HOST = "localhost"
LISTEN_PORT = 8000

receiver = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
receiver.bind((LISTEN_HOST, LISTEN_PORT))

expected_seq = 0
ack_drop_simulated = False

print("\n=== Stop-and-Wait Receiver Started ===")
print(f"Listening on {LISTEN_HOST}:{LISTEN_PORT} ...\n")

while True:
    raw_data, sender_address = receiver.recvfrom(1024)
    frame = raw_data.decode()

    seq_str, message = frame.split(":", 1)
    seq_num = int(seq_str)

    print("-" * 45)
    print(f"  Frame Received  -> {frame}")

    if seq_num == expected_seq:
        print(f"  Correct frame (seq={seq_num}). Delivering message: '{message}'")

        if message.lower() == "abc" and not ack_drop_simulated:
            print("[SIMULATION] ACK intentionally dropped (not sent)")
            ack_drop_simulated = True

        else:
            ack = f"ACK{seq_num}"
            receiver.sendto(ack.encode(), sender_address)
            print(f"  ACK Sent        -> {ack}")
            print("-" * 45 + "\n")

            ack_drop_simulated = False

            expected_seq = 1 - expected_seq

    else:
        prev_ack = f"ACK{1 - expected_seq}"
        receiver.sendto(prev_ack.encode(), sender_address)
        print(f"  Duplicate frame (seq={seq_num}, expected={expected_seq}). "
              f"Re-sending previous ACK -> {prev_ack}")
        print("-" * 45 + "\n")
