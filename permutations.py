# Time:  O(n * n!)
# Space: O(n)
#
# Given a collection of numbers, return all possible permutations.
# 
# For example,
# [1,2,3] have the following permutations:
# [1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], and [3,2,1].
#


class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def permute(self, array):
        result = []
        used = [False] * len(array)
        self.permuteRecu(result, used, [], array)
        return result
    
    def permuteRecu(self, result, used, cur, num):
        if len(cur) == len(num):
            result.append(cur + [])
            return
        for i in range(len(num)):
            if not used[i]:
                used[i] = True
                cur.append(num[i])
                self.permuteRecu(result, used, cur, num)
                cur.pop()
                used[i] = False


def permutation_rec(arr):
    # O(n!* n^2) time and O(n * n!) space
    perms = []
    permute_helper(arr, [], perms)
    return perms


def permute_helper(arr, perm, perms):
    n = len(arr)
    if n == 0:
        perms.append(perm) # it will run O(n!) times
    else:
        for i in range(n):
            # creating new arrays are killer taking O(n) time
            new_arr = arr[:i] + arr[i+1:]
            new_perm = perm + [arr[i]]
            permute_helper(new_arr, new_perm, perms)


def permutation(arr):
    perms = []
    permutate_helper(0, arr, perms)
    return perms


def permutate_helper(i, arr, perms):
    if i == len(arr) -1:
        perms.append(arr[:]) # copy the array, not use it
    else:
        for j in range(i, len(arr)):
            swap(arr, i, j)
            permutate_helper(i+1, arr, perms)
            swap(arr, j, i)


def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


if __name__ == "__main__":
    # print(Solution().permute([1, 2, 3]))
    # print(permutation_rec([1,2,3]))
    # arr1 = [1,2,3]
    # print(arr1[:1]+arr1[2:])
    print(permutation([1,2,3]))
