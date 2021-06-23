"""
Given the heigh of a staircase(h) and the maximum number of steps(k)
that you can climb up at a time.
Return the number of ways in which you can climb the staircase.
For example, clime_staircase(h=4, k = 2) -> 5
There are 5 ways:
(1,1,1,1),
(1,1,2),
(1,2,1),
(2,1,1),
(2,2)
FOLLOW UP: O(n) time is required.
"""

# Time:  O(n)
# Space: O(1)
#
# You are climbing a stair case. It takes n steps to reach to the top.
# Each time you can either climb 1 or 2 steps. 
# In how many distinct ways can you climb to the top?
#

class Solution:
    # @param n, an integer
    # @return an integer
    def climbStairs(self, n):
        prev, current = 0, 1
        for i in range(n):
            prev, current = current, prev + current, 
        return current


def climb_stair_terrible(h, k):
    # O(k^n) time and O(n) space
    if h <= 1:
        return 1
    ways = 0
    for i in range(1, min(k, h)+1):
        ways += climb_stair_terrible(h - i, k)
    return ways


def climb_stair_dp(h, k):
    # dynamic programming: O(k*h) time and O(h) space
    # record the ways to each height, records[0]=records[1]=1,
    records = [0] * (h+1)
    records[0] = 1  # b/c there's 1 way to get height 0.
    records[1] = 1  # and there's 1 way to get height 1.
    for i in range(2, h+1):
        down = 1
        while down <= k:
            records[i] += records[i - down]
            down += 1
    return records[h]


def clim_stair_sw(h, k):
    # O(n) time and O(n) space
    # sliding window of k, records[i] = records[i-1]*2 - records[i-1-k]
    records = [1] * (h + 1)
    for i in range(2, h + 1):
        if i <= k:
            records[i] = records[i-1] * 2
        else:
            records[i] = records[i - 1] * 2 - records[i - 1 - k]
    return records[h]

if __name__ == "__main__":
    # result = Solution().climbStairs(2)
    # print(climb_stair_terrible(4,3))
    print(climb_stair_dp(5, 3))
    print(clim_stair_sw(5, 3))
