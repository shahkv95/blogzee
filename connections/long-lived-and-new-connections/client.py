import socket
import time
from config import HOST, PORT, BUFFER_SIZE


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


def send_message(sock: socket.socket, message: str) -> str:
    print("sending................................")
    sock.sendall(message.encode())
    print("message sent...........................")

    time.sleep(5)

    response = sock.recv(BUFFER_SIZE).decode().strip()
    print("response received......................")

    return response


def long_lived_connection(host: str, port: int) -> None:
    print("Long Lived Connection established")
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        s.setblocking(False)  # Set the socket to non-blocking mode
        start_time = time.time()
        print(f'\nConnected to {host}:{port} in long-lived connection mode')

        for i in range(1, 5):
            try:
                message = f"Transaction {i} "
                print(f"\nSending {message}")
                response = send_message(s, message)
                print(f"Received \"Processed data: {response}\" from server")

            except ConnectionResetError:
                print('Connection reset by peer')
                break
            except ConnectionAbortedError:
                print('Connection aborted')
                break
            except BlockingIOError:
                # Socket is non-blocking, so a "Resource temporarily unavailable" error is expected
                pass
            except Exception as e:
                print(f'Error: {e}')
                break
        # s.close()
        end_time = time.time()
        print('Connection closed')
        print(
            f"Long-lived connection open for {end_time - start_time:.2f} seconds")


if __name__ == '__main__':
    host = HOST
    port = PORT

    new_connection(host, port)
    long_lived_connection(host, port)
