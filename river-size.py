def riverSizes(matrix):
    sizes = []
    visited = [[False for r in row] for row in matrix]
    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            if visited[r][c]:
                continue
            traverse_node(r, c, matrix, visited, sizes)
    return sizes


def traverse_node(i, j, matrix, visited, sizes):
    size = 0
    queue = [[i,j]]
    while len(queue):
        node = queue.pop()
        i, j = node
        # print("pop matrix[", i, ' ,', j, ']=',matrix[i][j])
        if visited[i][j]:
            continue
        visited[i][j] = True
        if matrix[i][j] == 0:
            continue
        size += 1
        unvisited_neighbors = get_unvisited_neighbors(i, j, matrix, visited)
        queue.extend(unvisited_neighbors)
        # for child in unvisited_neighbors:
        #     print('append([',child,']')
        #     queue.append(child)
    if size > 0:
        sizes.append(size)


def get_unvisited_neighbors(i, j, matrix, visited):
    unvisited_neighbors = []
    if i > 0 and not visited[i-1][j]:
        unvisited_neighbors.append([i-1,j])
    if i < len(matrix) - 1 and not visited[i+1][j]:
        unvisited_neighbors.append([i+1,j])
    if j > 0 and not visited[i][j-1]:
        unvisited_neighbors.append([i,j-1])
    if j < len(matrix[0]) -1 and not visited[i][j+1]:
        unvisited_neighbors.append([i,j+1])
    return unvisited_neighbors


def wrap_matrix(matrix):
    row = len(matrix)
    col = len(matrix[0])
    result = [[0 for c in range(col+2)] for r in range(row+2)]
    for r in range(row):
        for c in range(col):
            result[r+1][c+1] = matrix[r][c]
    return result


def print_matrix(matrix):
    for i in range(len(matrix)):
        print(matrix[i])

if __name__ == "__main__":
    river2 = [
        [1, 1, 0, 0, 0, 0, 1, 1],
        [1, 0, 1, 1, 1, 1, 0, 1],
        [0, 1, 1, 0, 0, 0, 1, 1]
    ]
    river1 = [
        [1,1,1,1],
        [1,1,1,1],
        [1,1,1,1]
    ]
    print(riverSizes(river2))
