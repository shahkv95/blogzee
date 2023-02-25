import socket
import time
from config import HOST, PORT, BUFFER_SIZE


def new_connection():
    print("\n----------------------------------------------------------------")
    print("\nNew Connection established")

    for i in range(2):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

            start_time = time.time()

            s.connect((HOST, PORT))
            s.sendall(f'Hello, server! Request number is {i}'.encode())

            time.sleep(0.1)

            data = s.recv(BUFFER_SIZE)
            print(f'\nResponse from server: {data.decode()}')

            end_time = time.time()
            print(
                f"New connection open for {end_time - start_time:.2f} seconds")


def send_message(sock: socket.socket, message: str) -> str:
    sock.sendall(message.encode())
    print("message sent...........................")

    time.sleep(2)

    response = sock.recv(BUFFER_SIZE).decode().strip()
    print("response received......................")

    return response


def long_lived_connection():
    print("\n----------------------------------------------------------------")
    print("\nLong Lived Connection established")
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.setblocking(False)  # Set the socket to non-blocking mode
        start_time = time.time()
        print(f'\nConnected to {HOST}:{PORT} in long-lived connection mode')

        for i in range(1, 5):
            # time.sleep(10)
            try:

                message = f"Transaction {i} "
                print(f"\nSending {message}")

                response = send_message(s, message)

                print(f"Received \"{response}\" from server")

            except ConnectionResetError:
                print('Connection reset by peer')
                break
            except ConnectionAbortedError:
                print('Connection aborted')
                break
            except BlockingIOError:
                # Socket is non-blocking, so a non-blocking exception is raised
                pass

            print(f"Transaction {i} complete")

        end_time = time.time()
        print(
            f"\nLong lived connection open for {end_time - start_time:.2f} seconds")


if __name__ == '__main__':
    new_connection()
    long_lived_connection()
