# Time:  O(n)
# Space: O(n)
#
# All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T,
# for example: "ACGAATTCCG". When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.
#
# Write a function to find_root all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.
#
# For example,
#
# Given s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT",
#
# Return:
# ["AAAAACCCCC", "CCCCCAAAAA"].
#

class Solution:
    # @param s, a string
    # @return a list of strings
    def findRepeatedDnaSequences(self, s):
        dict = {}
        rolling_hash = 0
        res = []

        for i in xrange(len(s)):
            rolling_hash = rolling_hash << 3 & 0x3fffffff | ord(s[i]) & 7
            if dict.get(rolling_hash) is None:
                dict[rolling_hash] = True
            else:
                if dict[rolling_hash]:
                    res.append(s[i - 9: i + 1])
                    dict[rolling_hash] = False
        return res

if __name__ == "__main__":
    print Solution().findRepeatedDnaSequences("AAAAAAAAAA")
    print Solution().findRepeatedDnaSequences("")
    print Solution().findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT")
