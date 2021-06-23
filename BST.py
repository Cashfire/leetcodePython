# Do not edit the class below except for
# the push, contains, and pop methods.
# Feel free to add new properties and methods
# to the class.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        curr_node = self
        while curr_node is not None:
            if value < curr_node.value:
                nxt_node = curr_node.left
                if nxt_node is None:
                    curr_node.left = BST(value)
                    break
            else:
                nxt_node = curr_node.right
                if nxt_node is None:
                    curr_node.right = BST(value)
                    break
            curr_node = nxt_node
        # Do not edit the return statement of this method.
        return self

    def contains(self, value):
        curr_node = self
        while curr_node is not None:
            if value == curr_node.value:
                return True
            elif value < curr_node.value:
                curr_node = curr_node.left
            else:
                curr_node = curr_node.right
        return False


    def remove(self, value, parent=None):
        if self is None:
            return self
        curr_node = self
        while curr_node is not None:
            if value < curr_node.value:
                parent = curr_node
                curr_node = curr_node.left
            elif value > curr_node.value:
                parent = curr_node
                curr_node = curr_node.right
            else:
                # if curr_node is a leaf
                if curr_node.left is None and curr_node.right is None:
                    if parent is None:
                        return self
                    elif parent.left == curr_node:
                        parent.left = None
                    else:
                        parent.right = None
                # if curr_node has 2 children
                elif curr_node.left is not None and curr_node.right is not None:
                    curr_node.value = curr_node.right.get_inorder_predecessor_val()
                    curr_node.right.pop(curr_node.value, curr_node)
                # if curr_node has 1 child
                elif curr_node.left is not None:
                    if parent is None:
                        curr_node.value = curr_node.left.value
                        curr_node.right = curr_node.left.right
                        curr_node.left = curr_node.left.left
                    elif parent.left == curr_node:
                        parent.left = curr_node.left
                    else:
                        parent.right = curr_node.left
                else:
                    if parent is None:
                        curr_node.value = curr_node.right.value
                        curr_node.left = curr_node.right.left
                        curr_node.right = curr_node.right.right
                    elif parent.left == curr_node:
                        parent.left = curr_node.right
                    else:
                        parent.right = curr_node.right
                curr_node = None
        # Do not edit the return statement of this method.
        return self

    def get_inorder_predecessor_val(self):
        curr = self
        while curr.left is not None:
            curr = curr.left
        return curr.value

    def print_bst(self):
        print(self.inorder_traverse())

    def inorder_traverse(self):
        result = []
        if self is None:
            return result
        if self.left is not None:
            result = self.left.inorder_traverse()
        result.append(self.value)
        if self.right is not None:
            result.extend(self.right.inorder_traverse())
        return result


def inorder_traverse(tree, array=None):
    if array is None:
        array = []
    if tree is not None:
        inorder_traverse(tree.left, array)
        array.append(tree.value)
        inorder_traverse(tree.right, array)
    return array


def validateBst(tree, minV=float('-inf'), maxV=float('inf')):
    if tree is None:
        return True
    if tree.value < minV or tree.value >= maxV:
        return False
    left_valid = validateBst(tree.left, minV, tree.value)
    return left_valid and validateBst(tree.right, tree.value, maxV)




if __name__ == "__main__":
    bst1 = BST(10)
    bst1.insert(9)
    bst1.insert(8)
    bst1.insert(11)
    bst1.insert(12)
    bst1.insert(10)
    bst1.print_bst()
    print(inorder_traverse(bst1))
    print(bst1.contains(10))
    bst1.remove(10)
    print(bst1.contains(10))
    bst1.print_bst()
    print(inorder_traverse(bst1))
    print(inorder_traverse(bst1, []))

    # print(python_func(3))
    # print(python_func(3))
