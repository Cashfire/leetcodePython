"""
given 2 non-empty arrays of integers, find_root the pairs of integers (one from each array)
whose absolute difference is closest to zero.
Input:

"""


def smallest_diff(a1, a2):
    # O(nlogn + mlogm) time due to sort
    # O(1) space
    a1.sort()
    a2.sort()
    l1 = 0
    l2 = 0
    smallest = float("inf")
    result = None
    while l1 < len(a1) and l2 < len(a2):
        n1, n2 =  a1[l1], a2[l2]
        if n1 == n2:
            return [n1, n2]
        elif n1 < n2:
            l1 += 1
        else:
            l2 += 1
        if abs(n1 - n2) < smallest:
            result = [n1, n2]
    return result


if __name__ == "__main__":
    arr1 = [1, 5, 9]
    arr2 = [3, 4, 5]
    print(smallest_diff(arr1, arr2))
