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