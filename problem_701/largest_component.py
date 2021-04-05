def is_valid(x, y, key, input):
    if x < n and y < m and x >= 0 and y >= 0:
        if visited[x][y] == 0 and input[x][y] == key:
            return True
        else:
            return False
    else:
        return False


def BFS(x, y, i, j, input):
    global COUNT

    if x != y:
        return

    visited[i][j] = 1
    COUNT += 1

    x_move = [ 0, 0, 1, -1 ]
    y_move = [ 1, -1, 0, 0 ]

    for u in range(4):
        # print(visited)
        print(result)
        if is_valid(i + y_move[u], j + x_move[u], x, input):
            BFS(x, y, i + y_move[u], j + x_move[u], input)


def reset_visited():
    for i in range(n):
        for j in range(m):
            visited[i][j] = 0


def reset_result(key, input):
    for i in range(n):
        for j in range(m):
            if visited[i][j] != 0 and input[i][j] == key:
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


def computeLargestConnectedGrid(input):
    global COUNT
    current_max = -10000000000

    for i in range(n):
        for j in range(m):
            reset_visited()
            COUNT = 0

            if j + 1 < m:
                BFS(input[i][j], input[i][j + 1], i, j, input)

            if COUNT >= current_max:
                current_max = COUNT
                reset_result(input[i][j], input)

            reset_visited()
            COUNT = 0

            if i + 1 < n:
                BFS(input[i][j], input[i + 1][j], i , j, input)

            if COUNT >= current_max:
                current_max = COUNT
                reset_result(input[i][j], input)

            # if

    print_result(current_max)
    return current_max


if __name__ == '__main__':
    from problem_701.Rectangle import Rectangle
    n = 2
    m = 2

    # n = 6
    # m = 8

    visited = [[0 for j in range(m)] for i in range(n)]

    result = [[0 for j in range(m)] for i in range(n)]

    COUNT = 0


    # input = [
    #             [ 0, 0, 0, 0, 0, 0, 0, 0 ],
    #             [ 0, 1, 1, 1, 0, 1, 1, 1 ],
    #             [ 1, 1, 1, 1, 0, 1, 0, 1 ],
    #             [ 0, 0, 1, 1, 0, 0, 0, 1 ],
    #             [ 0, 1, 0, 1, 1, 0, 0, 1 ],
    #             [ 1, 1, 0, 1, 1, 0, 0, 1 ]
    #         ]
    #
    # computeLargestConnectedGrid(input)

    # rectangle = Rectangle(n, m)
    #
    # for rec in rectangle.possible_arrays:
    #     largest_connected_grid = computeLargestConnectedGrid(rec)
    #     print(rec)
    #     print(largest_connected_grid)

    input = [[1, 0], [0, 0]]
    computeLargestConnectedGrid(input)