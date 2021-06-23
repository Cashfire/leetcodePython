# Time:  O(m * n)
# Space: O(1)
#
# Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.
# 
# For example,
# Given the following matrix:
# 
# [
#  [ 1, 2, 3 ],
#  [ 4, 5, 6 ],
#  [ 7, 8, 9 ]
# ]
# You should return [1,2,3,6,9,8,7,4,5].
#

class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of integers
    def spiralOrder(self, matrix):
        result = []
        if matrix == []:
            return result

        left, right, top, bottom = 0, len(matrix[0]) - 1, 0, len(matrix) - 1

        while left <= right and top <= bottom:
            for j in range(left, right + 1):
                result.append(matrix[top][j])
            for i in range(top + 1, bottom):
                result.append(matrix[i][right])
            for j in reversed(range(left, right + 1)):
                if top < bottom:
                    result.append(matrix[bottom][j])
            for i in reversed(range(top + 1, bottom)):
                if left < right:
                    result.append(matrix[i][left])
            left, right, top, bottom = left + 1, right - 1, top + 1, bottom - 1

        return result


def spiralTraverse(array):
    result = []
    left, right, top, bottom = 0, len(array[0])-1, 0, len(array)-1
    while top <= bottom and left <= right:
        for c in range(left, right+1):
            result.append(array[top][c])
        for r in range(top + 1, bottom):
            # it will do nothing range(start, stop) if start >= stop
            result.append(array[r][right])
        for c in reversed(range(left, right+1)):
            if top < bottom:
            # handle the corner case when a single row in the middle of matrix like arr2.
                result.append(array[bottom][c])
        for r in reversed(range(top + 1, bottom)):
            if left < right:
            # handle the corner case when a single column in the middle of matrix like arr3.
                result.append(array[r][left])
        left, right, top, bottom = left + 1, right -1, top + 1, bottom -1

    return result


def spiral_recursive(matrix):
    result = []
    spiral_fill(matrix, 0, len(matrix[0])-1, 0, len(matrix)-1, result)
    return result


def spiral_fill(matrix, left, right, top, bottom, result):
    if left > right or top > bottom:
        return
    for j in range(left, right + 1):
        result.append(matrix[top][j])
    for i in range(top + 1, bottom):
        result.append(matrix[i][right])
    for j in reversed(range(left, right + 1)):
        if top < bottom:
            result.append(matrix[bottom][j])
    for i in reversed(range(top + 1, bottom)):
        if left < right:
            result.append(matrix[i][left])
    spiral_fill(matrix, left + 1, right - 1, top + 1, bottom - 1, result)


def spiralTraverse(array):
    result = []
    left, right, top, bottom = 0, len(array[0])-1, 0, len(array)-1
    while top <= bottom and left <= right:
        for c in range(left, right+1):
            result.append(array[top][c])
        for r in range(top + 1, bottom):
            # it will do nothing range(start, stop) if start >= stop
            result.append(array[r][right])
        for c in reversed(range(left, right+1)):
            if top < bottom:
            # handle the corner case when a single row in the middle of matrix like arr2.
                result.append(array[bottom][c])
        for r in reversed(range(top + 1, bottom)):
            if left < right:
            # handle the corner case when a single column in the middle of matrix like arr3.
                result.append(array[r][left])
        left, right, top, bottom = left + 1, right -1, top + 1, bottom -1



if __name__ == "__main__":
    # print(Solution().spiralOrder([[ 1, 2, 3 ],
    #                               [ 4, 5, 6 ],
    #                               [ 7, 8, 9 ]]))
    # print(Solution().spiralOrder([[2,3]]))
    arr2 = [
        [1, 2, 3, 4],
        [10, 11, 12, 5],
        [9, 8, 7, 6]]
    arr3 = [
        [1, 2, 3],
        [12, 13, 4],
        [11, 14, 5],
        [10, 15, 6],
        [9, 8, 7]
    ]
    # print(Solution().spiralOrder(arr1))

    print(spiral_recursive(arr2))
    for i in range(2,2):
        print(i)
