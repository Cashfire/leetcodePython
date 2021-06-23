"""
We are given a binary tree (with root node root), a target node, and an integer value k.
Return a list of the values of all nodes that have a distance k from the target node.
The answer can be returned in any order.
"""
# Definition for a binary tree node.
import collections


class TreeNode:
    def __init__(self, x):
        self.value = x
        self.left = None
        self.right = None


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
    return nodes


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> list:
        def dfs(node, par=None):
            if node:
                node.par = par
                dfs(node.left, node)
                dfs(node.right, node)

        dfs(root)
        queue = collections.deque([(target, 0)])
        visited = {target}
        while queue:
            # poping 1st k-dist node means it gonna to add k+1 dist nodes now.
            if queue[0][1] == k:
                return [node.value for node, d in queue]
            node, d = queue.popleft()
            for nei in (node.par, node.left, node.right):
                if nei and nei not in visited:
                    visited.add(nei)
                    queue.append((nei, d+1))
        return []

    def distanceK2(self, root: TreeNode, target: TreeNode, k: int) -> list:
        result = []

        def dist_par_to_tar(node):
            # return distance from node's parent to the target
            if not node:  # if node is None
                return -1
            elif node is target:
                subtree_add(node, 0)
                return 1
            else:
                L, R = dist_par_to_tar(node.left), dist_par_to_tar(node.right)
                if L != -1:  # if find target in left subtree
                    if L == k:
                        result.append(node.value)
                    subtree_add(node.right, L + 1)
                    return R + 1
                elif R != -1:
                    if R == k:
                        result.append(node.value)
                    subtree_add(node.left, R + 1)
                    return R + 1
                return -1

        def subtree_add(node, dist):
            if not node or dist > k:
                return
            elif dist == k:
                result.append(node.value)
            else:
                subtree_add(node.left, dist + 1)
                subtree_add(node.right, dist + 1)

        dist_par_to_tar(root)
        return result



if __name__ == "__main__":
    arr1 = list(range(1,8))
    arr2 = [-1,2,3,4,5,6,7]
    nodes1 = build_tree(arr2)
    print(nodes1[4].value)
    print(Solution().distanceK(nodes1[0], nodes1[4], 2))
    print(Solution().distanceK2(nodes1[0], nodes1[4], 2))
