import socket
import json

HOST = "10.38.11.28"
PORT = 6000   # same as server

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

print(f"Connected to server on port {PORT}")

client_name = "Client of John Q. Smith"   # change to your name

while True:
    try:
        num = int(input("Enter an integer (1–100): "))
    except ValueError:
        print("Invalid input, try again.")
        continue

    data = {
        "name": client_name,
        "number": num
    }
    client_socket.send(json.dumps(data).encode())

    if not (1 <= num <= 100):
        print("Number out of range. Closing connection.")
        break

    reply = client_socket.recv(1024).decode()
    reply_data = json.loads(reply)

    server_name = reply_data["name"]
    server_number = reply_data["number"]

    # display
    print("\n--- Exchange ---")
    print(f"Client Name   : {client_name}")
    print(f"Server Name   : {server_name}")
    print(f"Client Number : {num}")
    print(f"Server Number : {server_number}")
    print(f"Sum           : {num + server_number}")

client_socket.close()

