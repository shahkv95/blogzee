import socket

host = '127.0.0.1'  # local IP address
port = 8080  # port to listen on

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
