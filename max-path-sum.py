"""
124. Binary Tree Maximum Path Sum <Hard>
A path in a binary tree is a sequence of nodes where each pair of adjacent nodes
in the sequence has an edge connecting them.
A node can only appear in the sequence at most once.
Note that the path does not need to pass through the root.
The path sum of a path is the sum of the node's values in the path.
Given the root of a binary tree, return the maximum path sum of any path.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(array):
    n = len(array) - 1
    nodes = {}
    for i in range(n, -1, -1):
        node = TreeNode(array[i])
        nodes[i] = node
        right_idx = i*2 + 2
        if right_idx <= n:
            node.right = nodes[right_idx]
        if right_idx - 1 <= n:
            node.left = nodes[right_idx - 1]
    return nodes[0]


class Solution:
    def __init__(self):
        self.max_sum = float('-inf')

    def maxPathSum(self, root: TreeNode) -> int:
        # O(n) time b/c each node is visited only once
        # O(n) space for worst case the BT is not unbalanced at all.
        def max_gain(node):
            if not node:
                return 0
            left_gain = max(max_gain(node.left), 0)
            right_gain = max(max_gain(node.right), 0)
            gain = node.val + left_gain + right_gain  # max_path pass through root
            self.max_sum = max(gain, self.max_sum)
            return node.val + max(left_gain, right_gain)  # max_brach pass through root

        max_gain(root)
        return self.max_sum



if __name__ == "__main__":
    arr1 = list(range(1,8))
    arr2 = [-1,2,3,4,5,6,7]
    root1 = build_tree(arr2)
    print(Solution().maxPathSum(root1))




















