"""
Given a grid of (width, height), starts from grid[0][0] to grid[height][width],
and actions are only Right or Down. How many ways that you can traverse the grid?
Eg ways_to_traverse_grid(w=2, h=3) = 3
1, D, D, R
2, R, D, D
3, D, R, D
You can assume that w * h >= 2.(i.e. the grid will never be 1*1)
"""


def ways_traverse_grid_rec(w, h):
    # O(2^(n+m)) time. Why? Because the stack tree is (n+m) height.
    # Why stack tree is (n+m) height? see iPad notes
    # O(n+m) space
    if w == 1 or h == 1:
        return 1
    return ways_traverse_grid_rec(w-1, h) + ways_traverse_grid_rec(w, h-1)


def ways_traverse_grid(w, h):
    # dynamic programming solution: O(n*m) time and O(n*m) space
    matrix = [[1 for c in range(w)] for r in range(h)]
    for r in range(1, h):
        for c in range(1, w):
            matrix[r][c] = matrix[r-1][c] + matrix[r][c-1]
    return matrix[-1][-1]


def ways_traverse_grid(w, h):
    # magic math solution: O(n+m) time and O(1) space
    x_dist_to_end = w - 1
    y_dist_to_end = h - 1
    numerator = factorial(x_dist_to_end + y_dist_to_end)
    denominator = factorial(x_dist_to_end) * factorial(y_dist_to_end)
    return numerator// denominator


def factorial(num):
    result = 1
    for n in range(2, num+1):
        result *= n
    return result




if __name__ == "__main__":

    print(ways_traverse_grid_rec(4,3))
    print(ways_traverse_grid(4,3))
    print(ways_traverse_grid(4,3))
