
def multiStringSearch(bigString, smallStrings):
    trie = Trie()
    result_dict = {}
    for small in smallStrings:
        trie.insert(small)

    for i in range(len(bigString)):
        curr = trie.root
        for j in range(i, len(bigString)):
            char = bigString[j]
            if char not in curr:
                break
            curr = curr[char]
            if trie.end_symbol in curr:
                result_dict[curr[trie.end_symbol]] = True
    return [x in result_dict for x in smallStrings]


class Trie:
    def __init__(self):
        self.root = {}
        self.end_symbol = '*'

    def insert(self, string):
        curr = self.root
        for i in range(len(string)):
            if string[i] not in curr:
                curr[string[i]] = {}
            curr = curr[string[i]]
        curr[self.end_symbol] = string


if __name__ == "__main__":
    bigString1 = "this big"
    smallStrings1 = ['this', 'is', 'bigger']
    print(multiStringSearch(bigString1, smallStrings1))
