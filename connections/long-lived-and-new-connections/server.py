import socket
from config import HOST, PORT

host = HOST
port = PORT

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))
server_socket.listen(0)

print(f'Server listening on port {port}')

while True:
    client_socket, addr = server_socket.accept()
    print(f'Client connected from {addr}')

    data = client_socket.recv(1024)
    if not data:
        break

    print(f'Received data: {data.decode()}')
    response = f'Processed data: {data.decode()}'.encode()
    client_socket.sendall(response)

    client_socket.close()

server_socket.close()
