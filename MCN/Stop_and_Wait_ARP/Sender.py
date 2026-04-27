#Special test keywords (case-insensitive):

#    "lost frame" -> simulates a lost frame (first attempt only)
#    "lost ack"   -> simulates a lost ACK   (first attempt only)
#    "exit"       -> quit cleanly

import socket

RECEIVER_HOST = "localhost"
RECEIVER_PORT = 8000
TIMEOUT_SECS  = 3

sender = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
receiver_address = (RECEIVER_HOST, RECEIVER_PORT)

sender.settimeout(TIMEOUT_SECS)
seq_num = 0

print("\n=== Stop-and-Wait Sender Started ===")
print("Special keywords: 'lost frame' | 'lost ack' | 'exit'\n")
while True:
    messages = []
    print("Enter messages to send (type 'done' to send, 'exit' to quit):")
    while True:
        msg = input(f"  Message {len(messages) + 1}: ").strip()
        if msg.lower() == "exit":
            print("\nSender closed. Goodbye!")
            sender.close()
            exit()
        if msg.lower() == "done":
            break
        if msg:
            messages.append(msg)
    if not messages:
        print("No messages entered. Try again.\n")
        continue

    print(f"\n--- Sending {len(messages)} message(s) ---")

    for message in messages:
        frame = f"{seq_num}:{message}"

        frame_lost_simulated = False
        ack_lost_simulated   = False

        print("=" * 45)
        print(f"  Sending Message: '{message}'  [Seq={seq_num}]")
        print("-" * 45)

        while True:

            if message.lower() == "lost frame" and not frame_lost_simulated:
                print("[SIMULATION] Frame dropped (lost in network)")
                frame_lost_simulated = True

            else:
                sender.sendto(frame.encode(), receiver_address)
                print(f"  Frame Sent   -> {frame}")

            try:
                raw_ack, _ = sender.recvfrom(1024)
                received_ack = raw_ack.decode()

                if message.lower() == "lost ack" and not ack_lost_simulated:
                    print("[SIMULATION] ACK lost before reaching sender")
                    ack_lost_simulated = True
                    raise socket.timeout

                expected_ack = f"ACK{seq_num}"
                if received_ack == expected_ack:
                    print(f"  ACK Received -> {received_ack}  [Correct - Frame delivered!]")
                    print("-" * 45 + "\n")
                    seq_num = 1 - seq_num
                    break
                else:
                    print(f"  Unexpected ACK: {received_ack} (expected {expected_ack}). Ignoring...")

            except socket.timeout:
                print(f"  Timeout! No ACK in {TIMEOUT_SECS}s. Resending frame...\n")
    print(f"\n=== All {len(messages)} message(s) delivered successfully! ===")
    print("-" * 45 + "\n")
sender.close()