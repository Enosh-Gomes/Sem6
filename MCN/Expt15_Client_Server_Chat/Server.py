import socket

HOST = "0.0.0.0"   # Listen on all interfaces
PORT = 5000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((HOST, PORT))

server.listen(1)

print(f"\n[SERVER STARTED] Listening on port {PORT}...\n")

conn, addr = server.accept()

print(f"[CONNECTED] Client connected from {addr}\n")

while True:

    # Receive message from client
    client_msg = conn.recv(1024).decode()

    if client_msg.lower() == "exit":
        print("Client disconnected.")
        break

    print(f"Client: {client_msg}")

    # Send reply
    server_msg = input("Server: ")

    conn.send(server_msg.encode())

    if server_msg.lower() == "exit":
        print("Server closed chat.")
        break

conn.close()
server.close()