# This is an input class. Do not edit.
class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


# Feel free to add new properties and methods to the class.
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def setHead(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
            return
        self.insertBefore(self.head, node)

    def setTail(self, node):
        if self.tail is None:
            self.tail = node
            self.head = node
            return
        self.insertAfter(self.tail, node)

    def insertBefore(self, node, nodeToInsert):
        # Do Nothing if nodeToInsert is 1-node LL.
        if nodeToInsert == self.head and nodeToInsert == self.tail:
            return
        self.remove(nodeToInsert)
        nodeToInsert.prev = node.prev
        nodeToInsert.next = node
        if node.prev is None:
            self.head = nodeToInsert
        else:
            node.prev.next = nodeToInsert
        node.prev = nodeToInsert

    def insertAfter(self, node, nodeToInsert):
        # Do Nothing if nodeToInsert is 1-node LL.
        if nodeToInsert == self.head and nodeToInsert == self.tail:
            return
        self.remove(nodeToInsert)
        nodeToInsert.prev = node
        nodeToInsert.next = node.next
        if node.next is None:
            self.tail = nodeToInsert
        else:
            node.next.prev = nodeToInsert
        node.next = nodeToInsert

    def insertAtPosition(self, position, nodeToInsert):
        # head at position 1
        if position == 1:
            self.setHead(nodeToInsert)
            return
        i = 1
        curr = self.head
        while curr is not None and i < position:
            curr = curr.next
            i += 1
        if curr is not None:
            self.insertBefore(curr, nodeToInsert)
        else:
            self.setTail(nodeToInsert)

    def removeNodesWithValue(self, value):
        curr = self.head
        while curr is not None:
            node_to_remove = curr
            curr = curr.next
            if node_to_remove.value == value:
                self.remove(node_to_remove)

    def remove(self, node):
        if node == self.head:
            self.head = node.next
        if node == self.tail:
            self.tail = node.prev
        self.removeBindings(node)

    def containsNodeWithValue(self, value):
        curr = self.head
        while curr is not None and curr.value != value:
            curr = curr.next
        return curr is not None

    def removeBindings(self, node):
        if node.prev is not None:
            node.prev.next = node.next
        if node.next is not None:
            node.next.prev = node.prev
        node.prev = None
        node.next = None

    def print_dll(self):
        result= []
        curr = self.head
        while curr is not None:
            result.append(curr.value)
            curr = curr.next
        print(result)


if __name__ == "__main__":
    dll1 = DoublyLinkedList()
    nodes = []
    for i,v in enumerate([5,4,3,2,1,4]):
        nodes.append(Node(v))
        dll1.setHead(nodes[i])
    dll1.print_dll()
    nodes.append(Node(6))
    dll1.setTail(nodes[-1])
    dll1.print_dll()
    node3 = dll1.head.next.next
    node6 = node3.next.next.next
    dll1.insertBefore(node6, node3)
    dll1.print_dll()
    node3 = dll1.head.next.next
    node6 = node3.next.next.next
    dll1.insertAfter(node6, node3)
    dll1.print_dll()
    dll1.removeNodesWithValue(3)
    dll1.print_dll()

    dll1.remove(dll1.head.next)
    dll1.print_dll()
    print(dll1.containsNodeWithValue(5))
