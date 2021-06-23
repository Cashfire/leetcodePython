"""
A panlindrome is defined as a string that's written the same forward and backward.
Note that single-character strings are palindromes.
"""


def isPanlindrom_iterative(string):
    l = 0
    r = len(string) - 1
    while l < r:
        if string[l] != string[r]:
            return False
        l += 1
        r -= 1
    return True


def isPanlindrom_recursive(string):
    return isPanlindrom_rec_helper(string, 0, len(string)-1)


def isPanlindrom_rec_helper(string, l, r):
    if l >= r:
        return True
    if string[l] != string[r]:
        return False
    return isPanlindrom_rec_helper(string, l+1, r-1)


if __name__ == "__main__":
    arr = "abcdcba"
    print(isPanlindrom_iterative(arr))
    print(isPanlindrom_recursive(arr))
