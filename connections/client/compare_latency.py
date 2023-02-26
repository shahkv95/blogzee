import time
from typing import Callable


def compare_latency(func1: Callable, func2: Callable, num_runs: int = 10) -> None:
    """
    Compares the latency of two functions.

    Parameters:
    func1 (Callable): The first function to compare.
    func2 (Callable): The second function to compare.
    num_runs (int): The number of times to run each function to get an average latency.
    """

    # Get the latency of the first function
    func1_latency = []
    for i in range(num_runs):
        start_time = time.perf_counter()
        func1()
        end_time = time.perf_counter()
        func1_latency.append((end_time - start_time))

    # Get the latency of the second function
    func2_latency = []
    for i in range(num_runs):
        start_time = time.perf_counter()
        func2()
        end_time = time.perf_counter()
        func2_latency.append((end_time - start_time))

    # Print the results
    print(f'{"Connection Type":<30} {"Latency":<15}')
    print(f'{f"{func1.__name__}":<30} {f"{sum(func1_latency)/len(func1_latency):.5f}":<15}')
    print(f'{f"{func2.__name__}":<30} {f"{sum(func2_latency)/len(func2_latency):.5f}":<15}')
