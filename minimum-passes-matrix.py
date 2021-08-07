

def minimumPassesOfMatrix(matrix):
    queue = get_all_positive_pos(matrix)
    passes = 0
    while queue:
        size = len(queue)
        while size > 0:
            r,c = queue.pop(0)
            size -= 1
            neighbors = get_ajacent_pos(r, c, matrix)
            for pos in neighbors:
                if matrix[pos[0]][pos[1]] < 0:
                    matrix[pos[0]][pos[1]] *= -1
                    queue.append(pos)
        passes += 1
    return -1 if contains_negatives(matrix) else passes - 1


def get_ajacent_pos(r, c, matrix):
    result = []
    if r > 0:
        result.append([r - 1,  c])
    if r < len(matrix) - 1:
        result.append([r + 1, c])
    if c > 0:
        result.append([r, c - 1])
    if c < len(matrix[0]) - 1:
        result.append([r, c + 1])
    return result

def get_all_positive_pos(matrix):
    row_n, col_n = len(matrix), len(matrix[0])
    pos = []
    for r in range(row_n):
        for c in range(col_n):
            if matrix[r][c] > 0:
                pos.append([r,c])
    return pos


def contains_negatives(matrix):
    for row in matrix:
        for val in row:
            if val < 0:
                return True
    return False

if __name__ == "__main__":
    matrix1 = [
        [0, -1, -3, 2, 0],
        [1, -2, -5, -1, -3],
        [3, 0, 0, -4, -1]]
    matrix2 = [
        [1, 0, 0, -2, -3],
        [-4, -5, -6, -2, -1],
        [0, 0, 0, 0, -1],
        [1, 2, 3, 0, -2]]
    print(minimumPassesOfMatrix(matrix1))
    # print(get_ajacent_pos(1, 0, matrix1))
