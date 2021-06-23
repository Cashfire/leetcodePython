"""
Inputs are a non-empty array of distinct integers, and an integer representing targetSum.
Like, inputs = [12, 3, 1, 2, -6, 5, -8, 6], targetSum =0
output = [
  [-8, 2, 6],
  [-8, 3, 5],
  [-6, 1, 5]
]
"""
# brute_force takes O(n^3) because Cn_3 = n*(n-1)*(n-2)/3!


def threeNumberSum(array, targetSum):
    # O(n^2) time and O(n) space???
    triplets = []
    array.sort()
    for i in range(len(array)-2):
        if array[i] >= targetSum:
            return triplets
        l = i + 1
        r = len(array) - 1
        target = targetSum - array[i]
        while l < r:
            subtotal = array[l] + array[r]
            if subtotal == target:
                triplets.append([array[i], array[l], array[r]])
                l += 1
                r -= 1
            elif subtotal < target:
                l += 1
            else:
                r -= 1
    return triplets


if __name__ == "__main__":
    arr1 = [12, 3, 1, 2, -6, 5, -8, 6]
    t1 =0
    print(threeNumberSum(arr1, t1))
