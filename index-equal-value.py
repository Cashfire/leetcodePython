"""
Given a sorted array of distinct integers, return the first index that idx == array[idx]
"""
# O(logN) time & O(1) space
def indexEqualsValue(array):
    # distinct sorted array:
    # if val < idx: ignore left.
    # if val > idx: ignore right.
    l, r = 0, len(array)-1
    while l <= r:
        mid = (l + r) //2
        if array[mid] > mid:
            r = mid - 1
        elif array[mid] < mid:
            l = mid + 1
        else:
            if mid == 0:
                return mid
            if array[mid - 1] != mid - 1:
                return mid
            r = mid - 1
    return -1


if __name__ == "__main__":
    arr1 = [-12, 1,2,3,12]
    print(indexEqualsValue(arr1))
