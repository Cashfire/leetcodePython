# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

    def set_parent(self, parent):
        self.parent = parent


def findSuccessor(tree, node):
    # O(n) time and O(n) space
    inorder_list = []
    inorder_traverse(tree, array=inorder_list)
    for i, n in enumerate(inorder_list):
        if i == len(inorder_list) -1:
            return None
        if n == node:
            break
    return inorder_list[i+1]


def inorder_traverse(tree, array=None):
    if tree is None:
        return
    inorder_traverse(tree.left, array)
    array.append(tree)
    inorder_traverse(tree.right, array)


def find_successor(tree, node):
    if node.right is not None:
        return get_left_most_child(node.right)
    return get_right_most_parent(node.left)

def get_left_most_child(node):
    curr = node
    while curr.left is not None:
        curr = curr.left
    return curr


def get_right_most_parent(node):
    curr = node
    while curr.parent is not None and curr.parent.right == curr:
        curr = curr.parent
    return curr.parent


if __name__ == "__main__":
    arr1 = [1, 2,3, 4,5,6,7,8]
    n5 = BinaryTree(5)
    n4 = BinaryTree(4, left=n5)
    n5.set_parent(n4)
    n3 = BinaryTree(3, left=n4)
    n4.parent = n3
    n7 = BinaryTree(7)
    n8 = BinaryTree(8)
    n6 = BinaryTree(6, left=n7, right=n8)
    n7.set_parent(n6)
    n8.set_parent(n6)
    n2 = BinaryTree(2, left=n3, right=n6)
    n3.set_parent(n2)
    n6.set_parent(n2)
    n1 = BinaryTree(1,left=n2, right=n6)
    n2.set_parent(n1)
    n6.set_parent(n1)
    ans1 = findSuccessor(n1, n2)
    print(ans1.value)
