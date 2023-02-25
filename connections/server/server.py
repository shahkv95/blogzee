import socket
from config import HOST, PORT, BUFFER_SIZE


def handle_client(client_socket, addr):
    print(f'Client connected from {addr}')

    while True:
        data = client_socket.recv(BUFFER_SIZE)
        if not data:
            break

        print(f'Received data: {data.decode()}')
        response = f'Processed data: {data.decode()}'.encode()
        client_socket.sendall(response)

    client_socket.close()


def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((HOST, PORT))
    server_socket.listen()

    print(f'Server listening on port {PORT}')

    while True:
        client_socket, addr = server_socket.accept()
        handle_client(client_socket, addr)

    server_socket.close()


if __name__ == '__main__':
    start_server()
