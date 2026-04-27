#  Simulation keywords (use as message content):

#    "frame lost"  ->  that frame is NOT sent once; only that
#                      frame times out and is retransmitted.
#    "ack lost"    ->  the ACK for that frame is ignored once;
#                      only that frame times out and is
#                      retransmitted (window does NOT go back).
#    "exit"        ->  quit cleanly.
#

import socket
import time

RECEIVER_HOST = "localhost"
RECEIVER_PORT = 8000
WINDOW_SIZE   = 4
TIMEOUT_SECS  = 3
POLL_INTERVAL = 0.1

sender = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
receiver_address = (RECEIVER_HOST, RECEIVER_PORT)
sender.settimeout(POLL_INTERVAL)



print("\n=== Selective Repeat Sender Started ===")
print(f"Window Size : {WINDOW_SIZE}")
print(f"Timeout     : {TIMEOUT_SECS}s per frame")
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

    acked     = {}
    send_time = {}

    frame_lost_simulated = set()
    ack_lost_simulated   = set()

    while base < total_frames:

        while next_frame < base + WINDOW_SIZE and next_frame < total_frames:
            msg   = messages[next_frame]
            frame = f"{next_frame}:{msg}"

            if msg.lower() == "frame lost" and next_frame not in frame_lost_simulated:
                print(f"  [SIMULATION] Frame {next_frame} NOT sent (lost in network)")
                frame_lost_simulated.add(next_frame)
                send_time[next_frame] = time.time()
            else:
                sender.sendto(frame.encode(), receiver_address)
                send_time[next_frame] = time.time()
                print(f"  Frame Sent   -> seq={next_frame}  msg='{msg}'  "
                      f"[window: {base}..{min(base + WINDOW_SIZE - 1, total_frames - 1)}]")

            next_frame += 1

        try:
            raw_ack, _ = sender.recvfrom(1024)
            ack     = raw_ack.decode()
            ack_num = int(ack[3:])

            if (ack_num < total_frames and
                    messages[ack_num].lower() == "ack lost" and
                    ack_num not in ack_lost_simulated):
                print(f"  [SIMULATION] ACK{ack_num} lost in transit (ignored)")
                print(f"  Frame {ack_num} timer is still running...")
                ack_lost_simulated.add(ack_num)
                continue

            if not acked.get(ack_num, False):
                acked[ack_num] = True
                print(f"  ACK Received -> ACK{ack_num}  (frame {ack_num} delivered)")

                old_base = base
                while base < total_frames and acked.get(base, False):
                    base += 1
                if base > old_base:
                    print(f"  Window slides: base {old_base} -> {base}")

        except socket.timeout:
            for seq in range(base, next_frame):
                if not acked.get(seq, False):
                    elapsed = time.time() - send_time.get(seq, time.time())
                    if elapsed >= TIMEOUT_SECS:
                        msg   = messages[seq]
                        frame = f"{seq}:{msg}"
                        sender.sendto(frame.encode(), receiver_address)
                        send_time[seq] = time.time()
                        print(f"  Timeout! Retransmitting ONLY seq={seq}  msg='{msg}'")

    print(f"\n=== All {total_frames} frame(s) delivered successfully! ===")
    print("-" * 56 + "\n")