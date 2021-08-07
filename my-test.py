class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity or 1
        self.cache = {}
        self.size = 0
        self.LRU = DoublyLinkedList()

    def get(self, key: int) -> int:
        curr = self.cache.get(key)
        if curr is None:
            return -1
        self._update_LRU(curr)
        return curr.value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            curr = self.cache[key]
            curr.value = value
            # update LRU order
            self._update_LRU(curr)
        else:
            new_node = Node(key, value)
            if self.size < self.capacity:
                self.size += 1
            else:
                # cache is full, first remove the LRU node out
                node = self.LRU.remove_head()
                self.cache.pop(node.key, None)
            self.cache[key] = new_node
            self.LRU.add(new_node)

    def _update_LRU(self, node):
        if node == self.LRU.tail:
            return
        if node == self.LRU.head:
            self.LRU.head = self.LRU.head.nxt
        node.remove_bindings()
        self.LRU.add(node)


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.nxt = node
            node.prev = self.tail
            self.tail = node

    def remove_head(self):
        result = self.head
        if self.head is None:
            return result
        if self.head == self.tail:
            self.head = None
            self.tail = None
            return result
        self.head = self.head.nxt
        return result


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.nxt = None

    def remove_bindings(self):
        if self.prev is not None:
            self.prev.nxt = self.nxt
        if self.nxt is not None:
            self.nxt.prev = self.prev
        self.prev = None
        self.nxt = None


def shortenPath(path):
    #
    tokens = path.split('/')
    result = []
    i = 0
    if tokens[0] == '':
        result.append('')
    else:
        while i < len(tokens):
            if tokens[i] in ['.', '']:
                i += 1
                continue
            elif tokens[i] == '..':
                result.append('..')
                i += 1
            else:
                break

    for j in range(i, len(tokens)):
        if tokens[j] in ['.', '']:
            continue
        elif tokens[j] == '..':
            # "/.." => "/"
            if len(result) > 0 and  result[-1] == '':
                continue
            if len(result) == 0 or result[-1] == '..':
                result.append('..')
            else:
                result.pop()
        else:
            result.append(tokens[j])
    if len(result) == 1 and result[0] == '':
        return '/'
    return '/'.join(result)
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
if __name__ == "__main__":
    # cache1 = LRUCache(2)
    # cache1.put(2,1)
    # cache1.put(3,2)
    # print(cache1.get(3))
    # print(cache1.get(2))
    # cache1.put(4,3)
    # print(cache1.get(2))
    # print(cache1.get(3))
    # print(cache1.get(4))

    # cache2 = LRUCache(4)
    # arr2 = [('a',1), ('b',2), ('c',3), ('d',4)]
    # for ele in arr2:
    #     cache2.put(ele[0], ele[1])
    # print(cache2.get('a'))
    # cache2.put('e', 5)
    # print(cache2.get('a'))

    path1 = "/foo/../test/../test/../foo//bar/./baz"
    path2 = './..'
    print(shortenPath(path2))
