#"frame lost"  ->  that frame is dropped ONCE by the sender.

#                      Receiver gets the next frame out of order,
#                      discards it, and sender times out & goes back.
#    "ack lost"    ->  receiver sends the ACK, but sender ignores it
#                      ONCE.  Sender times out and retransmits the
#                      entire window from base.
#    "exit"        ->  quit cleanly after the current batch.

import socket

RECEIVER_HOST = "localhost"
RECEIVER_PORT = 8000
WINDOW_SIZE   = 4
TIMEOUT_SECS  = 3

sender = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
receiver_address = (RECEIVER_HOST, RECEIVER_PORT)
sender.settimeout(TIMEOUT_SECS)

print("\n=== Go-Back-N Sender Started ===")
print(f"Window Size : {WINDOW_SIZE}")
print(f"Timeout     : {TIMEOUT_SECS}s")
print("Simulation keywords: 'frame lost' | 'ack lost' | 'exit'\n")

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

    total_frames = len(messages)
    print(f"\n--- Sending {total_frames} frame(s) with window size {WINDOW_SIZE} ---")

    base       = 0
    next_frame = 0
    frame_lost_simulated = set()
    ack_lost_simulated   = set()

    while base < total_frames:
        while next_frame < base + WINDOW_SIZE and next_frame < total_frames:
            msg = messages[next_frame]
            frame = f"{next_frame}:{msg}"

            if msg.lower() == "frame lost" and next_frame not in frame_lost_simulated:
                print(f"  [SIMULATION] Frame {next_frame} NOT sent (lost in network)")
                frame_lost_simulated.add(next_frame)
            else:
                sender.sendto(frame.encode(), receiver_address)
                print(f"  Frame Sent   -> seq={next_frame}  msg='{msg}'  "
                      f"[window: {base}..{min(base + WINDOW_SIZE - 1, total_frames - 1)}]")

            next_frame += 1

        try:
            raw_ack, _ = sender.recvfrom(1024)
            ack = raw_ack.decode()
            ack_num = int(ack[3:])

            if (ack_num < total_frames and
                    messages[ack_num].lower() == "ack lost" and
                    ack_num not in ack_lost_simulated):
                print(f"  [SIMULATION] ACK{ack_num} lost in transit (ignored by sender)")
                print(f"  Waiting for next cumulative ACK to cover it...")
                ack_lost_simulated.add(ack_num)
                continue

            if ack_num >= base:
                print(f"  ACK Received -> {ack}  "
                      f"[frames 0..{ack_num} acknowledged]")
                base = ack_num + 1
            else:
                print(f"  Duplicate/Old ACK: {ack} (base is {base}). Ignoring.")

        except socket.timeout:
            print(f"\n  Timeout! No ACK in {TIMEOUT_SECS}s. "
                  f"Going back to frame {base}. "
                  f"Retransmitting frames {base}..{next_frame - 1}.\n")
            next_frame = base

    print(f"\n=== All {total_frames} frame(s) delivered successfully! ===")
    print("-" * 50 + "\n")