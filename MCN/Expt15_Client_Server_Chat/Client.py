import socket
SERVER_IP = "127.0.0.1"    #Change to server PC IP for different PCs
PORT = 5000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((SERVER_IP, PORT))

print("\n[CONNECTED TO SERVER]\n")

while True:

    # Send message
    msg = input("Client: ")

    client.send(msg.encode())

    if msg.lower() == "exit":
        print("Disconnected from server.")
        break

    # Receive reply
    server_reply = client.recv(1024).decode()

    if server_reply.lower() == "exit":
        print("Server closed chat.")
        break

    print(f"Server: {server_reply}")

client.close()