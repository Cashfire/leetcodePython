# Time:  O(n * n!)
# Space: O(n)
#
# Given a collection of numbers that might contain duplicates, return all possible unique permutations.
# 
# For example,
# [1,1,2] have the following unique permutations:
# [1,1,2], [1,2,1], and [2,1,1].
#

class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        result = []
        used = [False] * len(nums)
        self.permuteUniqueRecu(result, used, [], nums)
        return result
    
    def permuteUniqueRecu(self, result, used, cur, nums):
        if len(cur) == len(nums):
            result.append(cur + [])
            return
        for i in range(len(nums)):
            if not used[i] and not (i > 0 and nums[i-1] == nums[i] and used[i-1]):  # if both not used[i] and not(...) are true then skip, to avoid repeat, 
                                                                                    # i.e. used[i] = False, used[i-1] = True, nums[i-1] == nums[i]
                used[i] = True                                                      # How does it help avoid such repeated pattern as 122 when nums[i-1] == nums[i]?
                cur.append(nums[i])                                                 # The condition that used[i] = False, used[i-1] = True allows 122 to be accessed only once:
                self.permuteUniqueRecu(result, used, cur, nums)                     # Recall the tree,  1     2     3, in the above way, nodes @ positions [1, 2, 3] will be accessed but not @ [1,3,2]
                cur.pop()                                                           #                 /  \   / \   / \                                                                    
                used[i] = False                                                     #                2   3  1  3  1  2
                                                                                    #               /   /  /  /  /  /
                                                                                    #              3   2  3  1  2  1
class Solution2:
    # @param num, a list of integer
    # @return a list of lists of integers
    def permuteUnique(self, nums):
        solutions = [[]]
        
        for num in nums:
            next = []
            for solution in solutions:
                for i in range(len(solution) + 1):
                    candidate = solution[:i] + [num] + solution[i:]
                    if candidate not in next:
                        next.append(candidate)
                
            solutions = next 
            
        return solutions


if __name__ == "__main__":
    print(Solution().permuteUnique([1, 1, 2]))
    print(Solution().permuteUnique([1, -1, 1, 2, -1, 2, 2, -1]))


