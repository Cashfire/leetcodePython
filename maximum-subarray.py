# Time:  O(n)
# Space: O(1)
#
# Find the contiguous subarray within an array (containing at least one number) which has the largest sum.
# 
# For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
# the contiguous subarray [4,-1,2,1] has the largest sum = 6.
# 
# click to show more practice.
# 
# More practice:
# If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
#

class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxSubArray(self, A):
        global_max, local_max = float("-inf"), 0
        for x in A:
            local_max = max(0, local_max + x)
            global_max = max(global_max, local_max)
        return global_max


def kadane_algo(array):
    max_so_far_with_i = array[0]
    max_so_far = array[0]
    for i in range(1, len(array)):
        num = array[i]
        max_so_far_with_i = max(max_so_far_with_i+ num, num)
        max_so_far = max(max_so_far_with_i, max_so_far)
    return max_so_far


def kadane_algo_return_subarray(array):
    end_id = 0
    max_so_far_with_i = array[0]
    max_so_far = array[0]
    for i in range(1, len(array)):
        num = array[i]
        max_so_far_with_i = max(max_so_far_with_i+ num, num)
        if max_so_far_with_i > max_so_far:
            end_id = i
            max_so_far = max_so_far_with_i
    for i in reversed(range(0, end_id+1)):
        max_so_far -= array[i]
        if max_so_far == 0:
            return array[i: end_id+1]
    return array[0:end_id+1]


if __name__ == "__main__":
    print(Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
    print(kadane_algo([-2,1,-3,4,-1,2,1,-5,4]))
    print(kadane_algo([3,5,-9,1,3,-2,3,4,7,2,-9,6,3,1,-5,4]))
    print(sum(kadane_algo_return_subarray([3,5,-9,1,3,-2,3,4,7,2,-9,6,3,1,-5,4])))
    
