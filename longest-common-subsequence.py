"""
LCS/Longest Common Subsequence
Given 2 strings,
"""
def print_table(matrix):
    for i in range(len(matrix)):
        print(matrix[i])


def longestCommonSubsequence(str1, str2):
    rows, cols = len(str1)+1, len(str2)+1
    matrix = [[0 for c in range(cols)] for r in range(rows)]
    for r in range(1, rows):
        for c in range(1, cols):
            if str1[r - 1] == str2[c - 1]:
                matrix[r][c] = matrix[r-1][c-1] + 1
            else:
                matrix[r][c] = max(matrix[r-1][c], matrix[r][c-1])
    # print_table(matrix)
    return build_seq(matrix, str1)

def build_seq(matrix, str1):
    seq = []
    r = len(matrix) - 1
    c = len(matrix[0]) - 1
    while r > 0 and c > 0:
        if matrix[r][c] == matrix[r-1][c]:
            r -= 1
        elif matrix[r][c] == matrix[r][c-1]:
            c -= 1
        else:
            seq.append(str1[r-1])
            r -= 1
            c -= 1
    return list(reversed(seq))


if __name__ == "__main__":
    # string1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    # string2 = "CCCDDEGDHAGKGLWAJWKJAWGKGWJAKLGGWAFWLFFWAGJWKAGTUV"
    # print(longestCommonSubsequence(string1, string2))
    # print(["C", "D", "E", "G", "H", "J", "K", "L", "W"])
    for i in range(3)+1:
        print(i)
