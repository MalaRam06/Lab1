# import socket

# server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# server_socket.bind(('localhost',8888))
# server_socket.listen()

# print("Server is listening on port 8888")
# conn,addr = server_socket.accept()
# print(f"Connected by {addr}")

# while True:
#   data = conn.recv(1024).decode()
#   nm=conn.recv(1024).decode()
#   num=conn.recv(1024).decode()
#   if not data or data.lower()=='exit':
#       print("Client disconnected.")
#       break
#   print(f"Client: {data}")
#   print(f"Client: {nm}")
#   print(f"Client: {num}")
#   reply = input("Server :")
#   name=input("")
#   nu=int(input(""))
#   sum=nu+num
#   conn.send(reply.encode())
#   conn.send(name.encode())
#   conn.send(nu.encode())
#   conn.send(sum.encode())

# conn.close()

# import socket
# import json

# server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server_socket.bind(('localhost', 8888))
# server_socket.listen()

# print("Server is listening on port 8888")
# conn, addr = server_socket.accept()
# print(f"Connected by {addr}")

# while True:
#     data = conn.recv(1024).decode()
#     if not data:
#         break
    
#     message = json.loads(data)  # decode JSON
#     msg = message["msg"]
#     name = message["name"]
#     num = message["num"]

#     if msg.lower() == "exit":
#         print("Client disconnected.")
#         break

#     print(f"Client message: {msg}")
#     print(f"Client name   : {name}")
#     print(f"Client number : {num}")

#     # prepare server response
#     reply_msg = input("Server message: ")
#     reply_name = input("Server name: ")
#     reply_num = int(input("Server number: "))

#     total = num + reply_num

#     response = {
#         "msg": reply_msg,
#         "name": reply_name,
#         "num": reply_num,
#         "sum": total
#     }

#     conn.send(json.dumps(response).encode())

# conn.close()

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
