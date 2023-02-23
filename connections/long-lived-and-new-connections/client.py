import socket
import time


def new_connection(host: str, port: int) -> None:
    print("New Connection established")

    for i in range(2):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

            start_time = time.time()

            s.connect((host, port))
            s.sendall(b'Hello, server! Request number is %d' % i)

            time.sleep(0.1)

            data = s.recv(1024)
            print(f'Response from server: {data.decode()}')

            end_time = time.time()
            print(
                f"New connection open for {end_time - start_time:.2f} seconds")


if __name__ == '__main__':
    host = '127.0.0.1'
    port = 8080

    new_connection(host, port)
