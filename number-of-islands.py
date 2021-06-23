# Time:  O(m * n)
# Space: O(m * n)
#
# Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. 
# An island is surrounded by water and is formed by connecting adjacent lands horizontally 
# or vertically. You may assume all four edges of the grid are all surrounded by water.
#
# Example 1:
#
# 11110
# 11010
# 11000
# 00000
# Answer: 1
#
# Example 2:
#
# 11000
# 11000
# 00100     
# 00011
# Answer: 3
#

class Solution:
    # @param {boolean[][]} grid a boolean 2D matrix
    # @return {int} an integer
    def numIslands(self, grid):
        if not grid:
            return 0

        row = len(grid)
        col = len(grid[0])
        used = [[False for j in range(col)] for i in range(row)]

        count = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1' and not used[i][j]:
                    self.dfs(grid, used, row, col, i, j) # finish one dfs search means an island has been found.
                    count += 1
        return count

    def dfs(self, grid, used, row, col, x, y):
        if grid[x][y] == '0' or used[x][y]:
            return
        used[x][y] = True

        if x != 0:
            self.dfs(grid, used, row, col, x - 1, y)  # up
        if x != row - 1:
            self.dfs(grid, used, row, col, x + 1, y)  # down
        if y != 0:
            self.dfs(grid, used, row, col, x, y - 1)  # left
        if y != col - 1:
            self.dfs(grid, used, row, col, x, y + 1)  # right


def removeIslands(matrix):
    # O(n*m) time and O(n*m) space
    row = len(matrix)
    col = len(matrix[0])
    connected_to_border = [[False for c in range(col)] for r in range(row)]
    for r in range(row):
        for c in range(col):
            row_is_border = r == 0 or r == row -1
            col_is_border = c == 0 or c == col -1
            is_border = row_is_border or col_is_border
            if not is_border:
                continue
            if matrix[r][c] == 1:
                update_border_matrix(r, c, matrix, connected_to_border)
    for r in range(1, row-1):
        for c in range(1, col-1):
            if connected_to_border[r][c]:
                continue
            matrix[r][c] = 0
    return matrix


def update_border_matrix(r, c, matrix, connected_to_border):
    # BFS
    queue = [(r,c)]
    while len(queue) > 0:
        r,c = queue.pop(0)
        is_visited= connected_to_border[r][c]
        if is_visited:
            continue
        connected_to_border[r][c] = True
        neighbors = get_neighbors(r,c, len(matrix), len(matrix[0]),connected_to_border)
        for neighbor in neighbors:
            row, col = neighbor
            if matrix[row][col] == 0:
                continue
            queue.append(neighbor)


def get_neighbors(r,c, row, col, connected_to_border):
    neighbors = []
    # UP
    if r-1 >= 0 and not connected_to_border[r-1][c]:
        neighbors.append((r-1, c))
    # DOWN
    if r + 1 < row and not connected_to_border[r+1][c]:
        neighbors.append((r+1, c))
    # LEFT
    if c - 1 >= 0 and not connected_to_border[r][c-1]:
        neighbors.append((r, c-1))
    # RIGHT
    if c + 1 < col and not connected_to_border[r][c+1]:
        neighbors.append((r, c+1))
    return neighbors


def print_matrix(matrix):
    for row in matrix:
        print(row)


def remove_islands(matrix):
    # O(n*m) time and O(1) space
    row = len(matrix)
    col = len(matrix[0])
    for r in range(row):
        for c in range(col):
            row_is_border = r == 0 or r == row -1
            col_is_border = c == 0 or c == col -1
            is_border = row_is_border or col_is_border
            if not is_border or matrix[r][c] != 1:
                continue
            # if matrix[r][c] != 1:
            # 	continue
            update_border_to_two(r, c, matrix)

    for r in range(1, row-1):
        for c in range(1, col-1):
            if matrix[r][c] == 1:
                matrix[r][c] = 0
    # change border cells back to 1
    for r in range(row):
        for c in range(col):
            if matrix[r][c] == 2:
                matrix[r][c] = 1
    return matrix


def update_border_to_two(r, c, matrix):
    queue = [(r,c)]
    while len(queue) > 0:
        r,c = queue.pop(0)
        matrix[r][c] = 2
        neighbors = get_neighbors1(r,c, len(matrix), len(matrix[0]))
        for neighbor in neighbors:
            row, col = neighbor
            if matrix[row][col] != 1:
                continue
            queue.append(neighbor)


def get_neighbors1(r,c, row, col):
    neighbors = []
    if r-1 >= 0:
        neighbors.append((r-1, c))
    if r + 1 < row:
        neighbors.append((r+1, c))
    if c -1 >= 0:
        neighbors.append((r, c-1))
    if c + 1 < col:
        neighbors.append((r, c+1))
    return neighbors


if __name__ == "__main__":
    graph1 = [
        [1, 0, 0, 0, 1, 0, 0, 0],
        [1, 0, 1, 0, 1, 0, 1, 0],
        [1, 1, 0, 1, 0, 0, 1, 0],
        [1, 1, 0, 1, 1, 0, 1, 0],
        [1, 0, 0, 0, 1, 0, 0, 0]
    ]
    print_matrix(remove_islands(graph1))

