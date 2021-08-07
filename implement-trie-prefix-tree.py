# Time:  O(n), per operation
# Space: O(1)
#
# Implement a trie with push, search, and startsWith methods.
#
# Note:
# You may assume that all inputs are consist of lowercase letters a-z.
#

class TrieNode:
    # Initialize your data structure here.
    def __init__(self):
        self.is_string = False
        self.leaves = {}
        

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        cur = self.root
        for c in word:
            if c not in cur.leaves:
                cur.leaves[c] = TrieNode()
            cur = cur.leaves[c]
        cur.is_string = True

    def search(self, word):
        res, node = self.childSearch(word)
        if res:
            return node.is_string
        return False        

    def startsWith(self, prefix):
        return self.childSearch(prefix)[0]

    def childSearch(self, word):
        cur = self.root
        for c in word:
            if c in cur.leaves:
                cur = cur.leaves[c]
            else:
                return False, None
        return True, cur

# Your Trie object will be instantiated and called as such:
# trie = Trie()
# trie.push("somestring")
# trie.search("key")

if __name__ == "__main__":
    trie1 = Trie()
    trie1.insert('this big')
    print(trie1.search('big'))
    # nodes = {}
    # nodes['b'] = {'c':{'*': True}}
    # nodes['a'] = {'b': nodes['b'].copy()}
    #
    # nodes['b']['a'] = nodes['a'].copy()
    # print(nodes['b'])

