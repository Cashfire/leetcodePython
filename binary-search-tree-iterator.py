# Time:  O(1)
# Space: O(h), h is height of binary tree
# 
# Implement an iterator over a binary search tree (BST).
# Your iterator will be initialized with the root node of a BST.
# 
# Calling next() will return the next smallest number in the BST.
# 
# Note: next() and hasNext() should run in average O(1) time
# and uses O(h) memory, where h is the height of the tree.
#

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BSTIterator:
    # @param root, a binary search tree's root node
    def __init__(self, root):
        self.stack = []
        self.cur = root

    # @return a boolean, whether we have a next smallest number
    def hasNext(self):
        return self.stack or self.cur

    # @return an integer, the next smallest number
    def next(self):
        while self.cur:
            self.stack.append(self.cur)
            self.cur = self.cur.left
        
        self.cur = self.stack.pop()
        node = self.cur
        self.cur = self.cur.right
        
        return node.val


def binary_search(array, target):
    # O(log(n)) time and O(1) space
    l = 0
    r = len(array) - 1
    while l <= r:
        mid = (r + l)//2
        curr = array[mid]
        if target == curr:
            return mid
        elif target > curr:
            l = mid + 1
        else:
            r = mid -1
    return -1


def binary_search_recursive(array, target):
    # O(log(n)) time and O(log(n)) space
    return bs_recursive_helper(array, target, 0, len(array) -1)


def bs_recursive_helper(array, target, l, r):
    if l > r:
        return -1
    mid = (l + r)//2
    num = array[mid]
    if num == target:
        return mid
    elif num > target:
        return bs_recursive_helper(array, target, mid+1, r)
    else:
        return bs_recursive_helper(array, target, l, mid-1)


if __name__ == "__main__":
    root = TreeNode(2)
    root.left = TreeNode(1)
    
    # Your BSTIterator will be called like this:
    # i, v = BSTIterator(root), []
    # while i.hasNext(): v.append(i.next())
    # print(v)

    arr = [1, 5, 23, 111]
    t = 120
    print(binary_search_recursive(arr, t))
