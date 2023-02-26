import socket
import time
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