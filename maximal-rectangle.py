# Time:  O(n^2)
# Space: O(n)
#
# Given a 2D binary matrix filled with 0's and 1's, 
# find_root the largest rectangle containing all ones and return its area.
#

class Solution:
    # @param matrix, a list of lists of 1 length string
    # @return an integer
    def maximalRectangle(self, matrix):
        if not matrix:
            return 0
        
        result = 0
        m = len(matrix)
        n = len(matrix[0])
        L = [0 for _ in range(n)]
        H = [0 for _ in range(n)]
        R = [n for _ in range(n)]

        for i in range(m):
            left = 0
            for j in range(n):
                if matrix[i][j] == '1':
                    L[j] = max(L[j], left)
                    H[j] += 1
                else:
                    L[j] = 0
                    H[j] = 0
                    R[j] = n
                    left = j + 1
                    
            right = n
            for j in reversed(range(n)):
                if matrix[i][j] == '1':
                    R[j] = min(R[j], right)
                    result = max(result, H[j] * (R[j] - L[j]))
                else:
                    right = j
                    
        return result


def max_rectangle_brutal_force(arr):
    # look left and right
    max_area = 0
    for i in range(len(arr)):
        height = arr[i]
        left, right = 0, 0
        for j in reversed(range(0, i)):
            if arr[j] < height:
                break
            else:
                left += 1
        for k in range(i + 1, len(arr)):
            if arr[k] < height:
                break
            else:
                right += 1
        max_area = max((left + right + 1) * height, max_area)
    return max_area


def max_rect(arr):
    # use stack to record non-exclusive left_bound,
    # and compute rectangle area when the idx cannot extend to right any longer.
    left_bounds = []
    max_area = 0
    for i, h in enumerate(arr + [0]):
        while left_bounds and h <= arr[left_bounds[-1]]:
            prev_h = arr[left_bounds.pop()]
            left = left_bounds[-1] if len(left_bounds) != 0 else -1
            width = i - left - 1
            max_area = max(max_area, width* prev_h)
        left_bounds.append(i)
    return max_area


if __name__ == "__main__":
    matrix = ["01101",
              "11010",
              "01110",
              "11110",
              "11111",
              "00000"]
    # print(Solution().maximalRectangle(matrix))

    arr1 = [1,3,2,2,1]
    print(max_rectangle_brutal_force(arr1))
    print(max_rect(arr1))
