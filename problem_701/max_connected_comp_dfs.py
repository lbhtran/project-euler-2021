# Program to count islands in boolean 2D matrix
class Graph:

    def __init__(self, row, col, g):
        self.ROW = row
        self.COL = col
        self.graph = g

    # A function to check if a given cell
    # (row, col) can be included in DFS
    def isSafe(self, i, j, visited):
        # row number is in range, column number
        # is in range and value is 1
        # and not yet visited
        return (i >= 0 and i < self.ROW and
                j >= 0 and j < self.COL and
                not visited[i][j] and self.graph[i][j])

    # A utility function to do DFS for a 2D
    # boolean matrix. It only considers
    # the 8 neighbours as adjacent vertices
    def DFS(self, i, j, visited, count=None):

        # These arrays are used to get row and
        # column numbers of 8 neighbours
        # of a given cell

        rowNbr = [0, 0, 1, -1]
        colNbr = [1, -1, 0, 0]

        # Mark this cell as visited
        visited[i][j] = True

        # Recur for all connected neighbours
        for k in range(4):
            if self.isSafe(i + rowNbr[k], j + colNbr[k], visited):
                count[0] += 1
                self.DFS(i + rowNbr[k], j + colNbr[k], visited, count)


    # The main function that returns
    # count of islands in a given boolean
    # 2D matrix
    def countIslands(self):
        # Make a bool array to mark visited cells.
        # Initially all cells are unvisited
        visited = [[False for j in range(self.COL)] for i in range(self.ROW)]

        # Initialize count as 0 and travese
        # through the all cells of
        # given matrix
        count = 0
        for i in range(self.ROW):
            for j in range(self.COL):
                # If a cell with value 1 is not visited yet,
                # then new island found
                if visited[i][j] == False and self.graph[i][j] == 1:
                    # Visit all cells in this island
                    # and increment island count
                    self.DFS(i, j, visited)
                    count += 1

        return count

    def largestRegion(self):

        # Make a bool array to mark visited cells.
        # Initially all cells are unvisited
        visited = [[0] * self.COL for i in range(self.ROW)]

        # Initialize result as 0 and travesle
        # through the all cells of given matrix
        result = 0
        for i in range(self.ROW):
            for j in range(self.COL):

                # If a cell with value 1 is not
                if (self.graph[i][j] and not visited[i][j]):
                    # visited yet, then new region found
                    count = [1]
                    self.DFS(i, j, visited, count)

                    # maximum region
                    result = max(result, count[0])
        return result


if __name__ == '__main__':
    import time
    import itertools
    from tqdm import tqdm
    import numpy as np

    tic = time.perf_counter()

    n = 4
    (row, col) = (n, n)

    total_rectangles = 0
    total_max_connected_grid_value = 0

    with tqdm(total=2**(n * n)) as pbar:

        for i in itertools.product([0, 1], repeat=n * n):
            rec = np.reshape(np.array(i), (n, n))
            g = Graph(row, col, rec)
            max_connected_grid = g.largestRegion()
            total_rectangles += 1
            total_max_connected_grid_value += max_connected_grid
            pbar.update(1)

    expected_max_connected_grid = total_max_connected_grid_value / total_rectangles

    toc = time.perf_counter()

    print()

    print(f"Calculation completed in {toc - tic:0.4f} seconds")

    print(f'Expected value: {round(expected_max_connected_grid, 8)}')
    print(f'Sum of all connected areas: {total_max_connected_grid_value}')
    print(f'Total search space: {total_rectangles}')
