# Time:  O(n)
# Space: O(n)
#
# Given a string containing just the characters '(', ')', '{', '}', '[' and ']',
# determine if the input string is valid.
# 
# The brackets must close in the correct order, "()" and "()[]{}" 
# are all valid but "(]" and "([)]" are not.
#

class Solution:
    # @return a boolean
    def isValid(self, s):
        stack, lookup = [], {"(": ")", "{": "}", "[": "]"}	
        for parenthese in s:
            if parenthese in lookup:      # if left bracket is detected, put into stack
                stack.append(parenthese)
            elif len(stack) == 0 or lookup[stack.pop()] != parenthese:    # after or: encounter right bracket, check dictionary, right left does not match.
                return False
        return len(stack) == 0
    
if __name__ == "__main__":
    print Solution().isValid("()[]{}")
    print Solution().isValid("()[{]}")