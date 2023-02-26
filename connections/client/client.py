from long_lived_connection import long_lived_connection
from compare_latency import compare_latency
from config import NUM_RUNS
from new_connection import new_connection


if __name__ == '__main__':

    compare_latency(new_connection, long_lived_connection, num_runs=NUM_RUNS)