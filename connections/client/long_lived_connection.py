import socket
import time
from config import HOST, PORT, BUFFER_SIZE

def send_message(sock: socket.socket, message: str) -> str:
    sock.sendall(message.encode())
    print("message sent...........................")

    time.sleep(0.1)

    response = sock.recv(BUFFER_SIZE).decode().strip()
    print("response received......................")

    return response


def long_lived_connection():
    print("\n----------------------------------------------------------------")
    print("\nLong Lived Connection established")
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.setblocking(False)  # Set the socket to non-blocking mode
        start_time = time.perf_counter()
        print(f'\nConnected to {HOST}:{PORT} in long-lived connection mode')

        for i in range(4):
            try:

                message = f"Transaction {i+1} "
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

            print(f"Transaction {i+1} complete")

        end_time = time.perf_counter()
        print(
            f"\nLong lived connection open for {end_time - start_time:.6f} seconds\n")