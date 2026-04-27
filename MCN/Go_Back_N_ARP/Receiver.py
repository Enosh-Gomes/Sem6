import socket

LISTEN_HOST = "localhost"
LISTEN_PORT = 8000

receiver = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
receiver.bind((LISTEN_HOST, LISTEN_PORT))

expected_seq = 0

print("\n=== Go-Back-N Receiver Started ===")
print(f"Listening on {LISTEN_HOST}:{LISTEN_PORT} ...\n")

while True:
    raw_data, sender_address = receiver.recvfrom(1024)
    frame = raw_data.decode()

    seq_str, message = frame.split(":", 1)
    seq_num = int(seq_str)

    print("-" * 50)
    print(f"  Frame Received -> seq={seq_num}  msg='{message}'")

    if seq_num == expected_seq:
        print(f"  In-order frame. Delivering message: '{message}'")

        ack = f"ACK{seq_num}"
        receiver.sendto(ack.encode(), sender_address)
        print(f"  ACK Sent       -> {ack}")
        print("-" * 50 + "\n")

        expected_seq += 1

    else:
        print(f"  Out-of-order frame! Expected seq={expected_seq}, "
              f"got seq={seq_num}. Discarding.")

        if expected_seq > 0:
            last_ack = f"ACK{expected_seq - 1}"
            receiver.sendto(last_ack.encode(), sender_address)
            print(f"  Re-sending last ACK -> {last_ack} "
                  f"(telling sender to go back to seq={expected_seq})")
        else:
            print("  No valid frame received yet. No ACK sent.")

        print("-" * 50 + "\n")