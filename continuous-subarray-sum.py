"""
leetcode 523
Given an integer array nums and an integer k,
return true if nums has a continuous subarray of size
at least two whose elements sum up to a multiple of k, or false otherwise.
checkSubarraySum([0,1,0], 2) -> False
checkSubarraySum([1,2,4], 4) -> False
"""

def checkSubarraySum(nums, k) -> bool:
    k_dict = {}
    total = 0
    for i in range(len(nums)):
        total = (nums[i] + total) % k
        if total == 0 and i > 0:
                return True
        cnt = k_dict.get(total, 0) + 1
        if cnt > 2 or (cnt == 2 and nums[i] % k != 0):
            return True
        k_dict[total] = cnt
    return False


if __name__ == "__main__":
    nums1 = [1,2,12]
    print(checkSubarraySum(nums1, 6) == False)
