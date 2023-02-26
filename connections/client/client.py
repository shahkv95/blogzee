import socket
import time, timeit
from config import HOST, PORT, BUFFER_SIZE


def new_connection():
    print("\n----------------------------------------------------------------")
    print("\nNew Connection established")

    for i in range(4):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

            start_time = time.perf_counter()

            s.connect((HOST, PORT))
            s.sendall(f'Hello, server! Request number is {i}'.encode())

            time.sleep(0.1)

            data = s.recv(BUFFER_SIZE)
            print(f'\nResponse from server: {data.decode()}')

            end_time = time.perf_counter()
            print(
                f"New connection open for {end_time - start_time:.6f} seconds")


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

import time


def compare_latency(nc, llc, num_runs=10):
    nc_latency = []
    for i in range(num_runs):
        start_time = time.perf_counter()
        nc()
        end_time = time.perf_counter()
        nc_latency.append((end_time - start_time))

    llc_latency = []
    for i in range(num_runs):
        start_time = time.perf_counter()
        llc()
        end_time = time.perf_counter()
        llc_latency.append((end_time - start_time))
    print("----------------------------------------------------------------")
    print(f'\n{"Connection Type":<30} {"Latency (s)":<15}')
    print(f'{f"New Connection":<30} {f"{sum(nc_latency)/len(nc_latency):.5f}":<15}')
    print(f'{f"Long-Lived Connection":<30} {f"{sum(llc_latency)/len(llc_latency):.5f}":<15}')


if __name__ == '__main__':

    # new_connection_elapsed_time = timeit.timeit(new_connection, number=1)
    # print(f"Elapsed time: {new_connection_elapsed_time:.6f} seconds")


    # long_lived_connection_elapsed_time = timeit.timeit(long_lived_connection, number=1)
    # print(f"Elapsed time: {long_lived_connection_elapsed_time:.6f} seconds")

    compare_latency(new_connection, long_lived_connection, num_runs=1)