# Time:  O(n)
# Space: O(1)
#
# Given an array of non-negative integers, you are initially positioned at the first index of the array.
# 
# Each element in the array represents your maximum jump length at that position.
# 
# Your goal is to reach the last index in the minimum number of jumps.
# 
# For example:
# Given array A = [2,3,1,1,4]
# 
# The minimum number of jumps to reach the last index is 2. (Jump 1 step from index 0 to 1, then 3 steps to the last index.)
#

class Solution:
    # @param A, a list of integers
    # @return an integer
    def jump(self, A):
        # NEAT!!!
        jump_count = 0
        max_reach = 0
        curr_jump_end = 0
        for i, length in enumerate(A):
            if i > max_reach:
                return -1
            if i > curr_jump_end:
                curr_jump_end = max_reach
                jump_count += 1
            max_reach = max(max_reach, i + length)

        return jump_count

# Time:  O(n^2)
# Space: O(1)     
class Solution2:
    # @param A, a list of integers
    # @return an integer
    def jump(self, A):
        result, prev_reachable, reachable = 0, -1, 0
        while reachable > prev_reachable:
            if reachable >= len(A) - 1:
                return result
            result += 1
            prev_reachable = reachable
            for i, length in enumerate(A[:reachable + 1]):
                reachable = max(reachable, i + length)
        return -1
    
if __name__ == "__main__":
    print(Solution().jump([2,3,1,1,4]))
    print(Solution().jump([3,2,1,0,4]))
    print(Solution().jump([0]))
