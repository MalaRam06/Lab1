import socket
import random

server_name = input("Server's name : ")
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 5001))
server_socket.listen(1)
print("Server is listening on port 5001...")

conn, addr = server_socket.accept()
print("Connected by", addr)

data = conn.recv(1024).decode()
client_name, client_number = data.split(',')
client_number = int(client_number)

print("Client's Name:", client_name)
print("Server's Name:", server_name)

# Check if the client's number is outside the allowed range
if not (1 <= client_number <= 100):
    print("Received number out of range! Closing connection.")
    conn.close()
    server_socket.close()
    exit()  # Terminate the program

# If the number is valid, proceed
server_number = random.randint(1, 100)
print("Client's Number:", client_number)
print("Server's Number:", server_number)
print("Sum:", client_number + server_number)

response = f"{server_name},{server_number}"
conn.send(response.encode())

# Close the connection after replying
conn.close()
server_socket.close()
