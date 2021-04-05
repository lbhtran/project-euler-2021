def is_valid(x, y, input):
    if x < n and y < m and x >= 0 and y >= 0:
        if visited[x][y] == 0 and input[x][y] == 1:
            return True
        else:
            return False
    else:
        return False


def BFS(x, y, i, j, input):
    global COUNT
    if x == 0:
        return

    if x != y and x == 1:
        COUNT = 1
        return

    visited[i][j] = 1
    COUNT += 1

    x_move = [0, 0, 1, -1]
    y_move = [1, -1, 0, 0]

    for u in range(4):
        if is_valid(i + y_move[u], j + x_move[u], input):
            BFS(x, y, i + y_move[u], j + x_move[u], input)


def reset_visited():
    for i in range(n):
        for j in range(m):
            visited[i][j] = 0


def reset_result(input):
    for i in range(n):
        for j in range(m):
            if visited[i][j] != 0 and input[i][j] == 1:
                result[i][j] = visited[i][j]
            else:
                result[i][j] = 0


def print_result(res):

    print(f'The largest connected component of the grid is : {str(res)}.')
    for i in range(n):
        for j in range(m):
            if result[i][j] != 0:
                print(result[i][j], end = ' ')

            else:
                print('. ', end = '')

        print()

def computeMaxConnectedGrid(input):
    global COUNT
    current_max = -10000000000

    for i in range(n):
        for j in range(m):
            reset_visited()
            COUNT = 0

            if j + 1 < m:
                BFS(input[i][j], input[i][j + 1], i, j, input)
            else:
                BFS(input[i][j], 1, i, j, input)

            if COUNT >= current_max:
                current_max = COUNT
                reset_result(input)

            reset_visited()
            COUNT = 0

            if i + 1 < n:
                BFS(input[i][j], input[i + 1][j], i, j, input)
            else:
                BFS(input[i][j], 1, i, j, input)

            if COUNT >= current_max:
                current_max = COUNT
                reset_result(input)

    return current_max


if __name__ == '__main__':
    import time
    from tqdm import tqdm

    tic = time.perf_counter()

    n = 4
    m = 4

    visited = [[0 for j in range(m)] for i in range(n)]

    result = [[0 for j in range(m)] for i in range(n)]

    COUNT = 0

    # input = [[0, 0], [0, 1]]
    # print(is_valid(1, 1, input))

    from problem_701.Rectangle import Rectangle

    # rectangle = Rectangle(n, m)

    import itertools
    import numpy as np

    total_rectangles = 0 # 2 ** (n * m)
    total_max_connected_grid_value = 0

    with tqdm(total=2**(n*m)) as pbar:

        for i in itertools.product([0, 1], repeat=m*n):
            rec = np.reshape(np.array(i), (m, n))

            max_connected_grid = computeMaxConnectedGrid(rec)
            # print(rec)
            # print(max_connected_grid)
            total_rectangles += 1
            total_max_connected_grid_value += max_connected_grid
            # print(total_rectangles)
            pbar.update(1)

    expected_max_connected_grid = total_max_connected_grid_value / total_rectangles

    toc = time.perf_counter()

    print()

    print(f"Calculation completed in {toc - tic:0.4f} seconds")

    print(f'Expected value: {round(expected_max_connected_grid, 8)}')
    print(f'Sum of all connected areas: {total_max_connected_grid_value}')
    print(f'Total search space: {total_rectangles}')