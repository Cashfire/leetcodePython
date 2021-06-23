# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.visited = False


def branch_sums(root):
    # O(n) time | O(n) space due to recursion
    sum_list = []
    branch_sums_Helper(root, 0, sum_list)
    return sum_list


def branch_sums_Helper(node, subtotal, sum_list):
    if node is None:
        return
    subtotal += node.value
    if node.left is None and node.right is None:
        sum_list.append(subtotal)
        return
    branch_sums_Helper(node.left, subtotal, sum_list)
    branch_sums_Helper(node.right, subtotal, sum_list)


# follow up: if the space is restricted to log(n)
def branch_sums_iterative(root):
    # iterative DFS: O(n) time | O(log(n)) space
    stack = [root]
    result = []
    total = root.value
    while len(stack) != 0:
        curr = stack[-1]
        while has_unvisited_child(curr, side="left") or has_unvisited_child(curr, side="right"):
            child = curr.left if has_unvisited_child(curr, side="left") else curr.right
            total += child.value
            stack.append(child)
            child.visited = True
            curr = child
        if is_leaf(curr):
            result.append(total)
        prev_val = stack.pop().value
        total -= prev_val
    return result


def has_unvisited_child(node, side="left"):
    if side == "left":
        return node.left is not None and node.left.visited == False
    else:
        return node.right is not None and node.right.visited == False


def is_leaf(node):
    return node.left is None and node.right is None


if __name__ == "__main__":
    print("test branch sums")
    bt = [None,1,2,3,4,5,6,7,8,9,10,None]
    bt_nodes = [None]

    for i in range(1, 11):
        bt_nodes.append(BinaryTree(bt[i]))

    for i in range(1, 5):
        bt_nodes[i].left = bt_nodes[2 * i]
        bt_nodes[i].right = bt_nodes[2* i + 1]
    bt_nodes[5].left = bt_nodes[10]
    print(branch_sums(bt_nodes[1]))


