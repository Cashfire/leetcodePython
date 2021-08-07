# Time:  O(n)
# Space: O(1)
#
# Given a string, find_root the length of the longest substring without repeating characters.
# For example, the longest substring without repeating letters for "abcabcbb" is "abc", which the length is 3. 
# For "bbbbb" the longest substring is "b", with the length of 1.
#

class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        longest, start, visited = 0, 0, [False for _ in range(256)]
        for i, char in enumerate(s):
            if visited[ord(char)]:
                while char != s[start]:
                    visited[ord(s[start])] = False
                    start += 1
                start += 1
            else:
                visited[ord(char)] = True
            longest = max(longest, i - start + 1)
        return longest


def longestSubstringWithoutDuplication(string):
    last_seen = {}
    longest = [0, 1]
    start_id = 0
    for i, char in enumerate(string):
        if char in last_seen:
            start_id = max(start_id, last_seen[char] + 1)
        if longest[1] - longest[0] < i - start_id + 1:
            longest = [start_id, i + 1]
        last_seen[char] = i
    return string[longest[0]: longest[1]]


if __name__ == "__main__":
    print(Solution().lengthOfLongestSubstring("abcabcbb"))
    print(longestSubstringWithoutDuplication('abcabcbb'))
    print(longestSubstringWithoutDuplication('clementl'))
