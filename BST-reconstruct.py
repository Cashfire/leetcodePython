
class BST:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

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


class TreeInfo:
    def __init__(self, rootId):
        self.rootId = rootId


def reconstruct_bst(preOrderlist):
    treeInfo = TreeInfo(0)
    return reconstruct_bst_helper(float('-inf'), float('inf'), preOrderlist, treeInfo)


def reconstruct_bst_helper(low, high, values, currSubtreeInfo):
    curr_id = currSubtreeInfo.rootId

    if curr_id == len(values):
        return None
    curr_val = values[curr_id]
    # print(curr_id*'   ','[(',low, ', ',high,'), i=',curr_id, ', val=', curr_val,']')
    if curr_val < low or curr_val >= high:
        return None
    currSubtreeInfo.rootId += 1
    leftSubtree = reconstruct_bst_helper(low, curr_val, values, currSubtreeInfo)
    rightSubtree = reconstruct_bst_helper(curr_val, high, values, currSubtreeInfo)
    # print("make root(", curr_val, ')')
    return BST(curr_val, leftSubtree, rightSubtree)


if __name__ == "__main__":
    arr1 = [10,4,2,1,4,7,19,18]
    bst1 = reconstruct_bst(arr1)
    bst1.print_bst()


    arr2 = [1, 2,3, 4,5,6,7,8]
    bst2 = reconstruct_bst(arr2)
    bst2.print_bst()
    # ans2 = findSuccessor(bst2, bst2.left)
    # print(ans2.value)


