# Time:  O(n)
# Space: O(n)
#
# Given an array of strings, return all groups of strings that are anagrams.
#
# Note: All inputs will be in lower-case.
#

class Solution:
    # @param strs, a list of strings
    # @return a list of strings
    def anagrams(self, strs):
        anagrams_map, result = {}, []
        for s in strs:
            sorted_str = ("").join(sorted(s))
            if sorted_str in anagrams_map:
                anagrams_map[sorted_str].append(s)
            else:
                anagrams_map[sorted_str] = [s]
        for anagram in anagrams_map.values():
            if len(anagram) > 1:
                result += anagram
        return result


def groupAnagrams(words):
    result = []
    while len(words) > 0:
        word = words.pop()
        result.append([word])
        dict1 = None
        i = 0
        while i < len(words):
            if len(words[i]) == len(word):
                if dict1 is None:
                    dict1 = get_dict(word)

                if is_anagrams(dict1, get_dict(words[i])):
                    result[-1].append(words[i])
                    words.pop(words[i])
                    i -= 1
            i += 1
    return result


def group_anagram(words):
    # O(n * W * logW) time, O(W*n)
    # n is len(words), W is len(longest_word).
    anagrams = {}
    for word in words:
        sorted_word = "".join(sorted(word))  # WlogW
        if sorted_word in anagrams:
            anagrams[sorted_word].append(word)
        else:
            anagrams[sorted_word] = [word]
    return list(anagrams.values())


def is_anagrams(dict1, dict2):
    if len(dict1.keys()) != len(dict2.keys()):
        return False

    for k,v in dict1.items():
        if dict2.get(k) is None:
            return False
        elif dict2.get(k) != v:
            return False
    return True


def get_dict(word):
    result = {}
    for c in word:
        result[c] = result.get(c, 0) + 1
    return result


if __name__ == "__main__":
    # result = Solution().anagrams(["cat", "dog", "act", "mac"])
    # print(result)
    # arr1 = ["yo", "act", "flop", "tac", "foo", "cat", "oy", "olfp"]
    # print(groupAnagrams(arr1))
    print(sorted("act"))

