import socket
import json

HOST = "10.38.11.28"
PORT = 6000   # must be > 5000 (as per assignment)

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen()

print(f"Server is listening on port {PORT}")
conn, addr = server_socket.accept()
print(f"Connected by {addr}")

server_name = "Server of John Q. Smith"   # change to your name
server_number = 42                        # fixed or random between 1–100

while True:
    data = conn.recv(1024).decode()
    if not data:
        break

    client_data = json.loads(data)
    client_name = client_data["name"]
    client_number = client_data["number"]

    # stop if number out of range
    if not (1 <= client_number <= 100):
        print("Invalid number received. Closing connection.")
        break

    # display
    print("\n--- Exchange ---")
    print(f"Client Name   : {client_name}")
    print(f"Server Name   : {server_name}")
    print(f"Client Number : {client_number}")
    print(f"Server Number : {server_number}")
    print(f"Sum           : {client_number + server_number}")

    # prepare reply
    reply = {
        "name": server_name,
        "number": server_number
    }
    conn.send(json.dumps(reply).encode())

conn.close()
server_socket.close()
