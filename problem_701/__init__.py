from problem_701.max_connected_comp_dfs import *
import multiprocessing

class Counter(object):
    def __init__(self):
        self.val = multiprocessing.Value('i', 0)

    def increment(self, n=1):
        with self.val.get_lock():
            self.val.value += n

    @property
    def value(self):
        return self.val.value

def process_expected_area(i):
    rec = np.reshape(np.array(i), (n, n))
    g = Graph(row, col, rec)
    max_connected_grid = g.largestRegion()
    total_rectangles.increment()
    total_max_connected_grid_value.increment(max_connected_grid)


if __name__ == '__main__':
    import time
    import itertools
    import numpy as np
    import math
    # from iteration_utilities import random_product

    tic = time.perf_counter()

    n = 7
    (row, col) = (n, n)

    total_rectangles = Counter()
    total_max_connected_grid_value = Counter()
    max_iter = 2**(n*n) # math.ceil(2**(n*n) / 10000000)
    iter_steps = 500000000 # 2**math.ceil((n*n)/2)

    try:
        p = itertools.product([0, 1], repeat=n*n)
        s = itertools.islice(p, 0, max_iter, iter_steps)
        max_number_processes = multiprocessing.cpu_count()
        print(f'Running with {max_number_processes} processes.')
        # print(f'Total search space is {len(s)}')
        pool = multiprocessing.Pool(max_number_processes)  # on max no of processors
        data_outputs = pool.map(process_expected_area, s)
    finally:  # To make sure processes are closed in the end, even if errors happen
        pool.close()
        pool.join()

    expected_max_connected_grid = total_max_connected_grid_value.value / total_rectangles.value

    toc = time.perf_counter()

    print()

    print(f"Calculation completed in {toc - tic:0.4f} seconds")

    print(f'Expected value: {round(expected_max_connected_grid, 8)}')
    print(f'Sum of all connected areas: {total_max_connected_grid_value.value}')
    print(f'Total search space: {total_rectangles.value}')