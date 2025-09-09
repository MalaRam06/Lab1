import socket

client_name = input("Client's name: ")
client_number = int(input("Enter a number between 1 and 100: "))

if not (1 <= client_number <= 100):
    print("Number out of range!")
    exit()

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 5001))

message = f"{client_name},{client_number}"
client_socket.send(message.encode())

data = client_socket.recv(1024).decode()
server_name, server_number = data.split(',')
server_number = int(server_number)

print("Client's Name:", client_name)
print("Server's Name:", server_name)
print("Client's Number:", client_number)
print("Server's Number:", server_number)
print("Sum:", client_number + server_number)

client_socket.close()
