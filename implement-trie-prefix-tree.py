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

    # @param {string} word
    # @return {void}
    # Inserts a word into the trie.
    def insert(self, word):
        cur = self.root
        for c in word:
            if not c in cur.leaves:
                cur.leaves[c] = TrieNode()
            cur = cur.leaves[c]
        cur.is_string = True

    # @param {string} word
    # @return {boolean}
    # Returns if the word is in the trie.
    def search(self, word):
        res, node = self.childSearch(word)
        if res:
            return node.is_string
        return False        

    # @param {string} prefix
    # @return {boolean}
    # Returns if there is any word in the trie
    # that starts with the given prefix.
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
    # nodes = {}
    # nodes['b'] = {'c':{'*': True}}
    # nodes['a'] = {'b': nodes['b'].copy()}
    #
    # nodes['b']['a'] = nodes['a'].copy()
    # print(nodes['b'])
    arr1 = [1,3,2,5,4]
    for i in range(1,len(arr1)-1):
        if arr1[i-1] < arr1[i] < arr1[i+1]:
            print('arr[',i,']=',arr1[i])
