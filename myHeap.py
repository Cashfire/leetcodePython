# Do not edit the class below except for the buildHeap,
# _siftdown, _siftup, peek, pop, and push methods.
# Feel free to add new properties and methods to the class.
class MinHeap:
    def __init__(self, array):
        # Do not edit the line below.
        self.heap = self.buildHeap(array)
        # self.length += 1
        # self.compare_func = compare_func

    def buildHeap(self, array):
        n = len(array)
        last_parent_id = (n - 1) //2
        for i in range(last_parent_id, -1, -1):
            self._siftdown(i, n - 1, array)
        return array

    def _siftdown(self, curr_id, end_id, heap):
        child1_id = curr_id * 2 + 1
        while child1_id <= end_id:
            child2_id = child1_id + 1 if child1_id + 1 <= end_id else -1
            if child2_id != -1 and heap[child2_id] < heap[child1_id]:
                id_to_swap = child2_id
            else:
                id_to_swap = child1_id
            if heap[id_to_swap] < heap[curr_id]:
                self.swap(id_to_swap, curr_id, heap)
                curr_id = id_to_swap
                child1_id = curr_id * 2 + 1
            else:
                return

    def _siftup(self, curr_id, heap):
        parent_id = (curr_id - 1)//2
        while parent_id >= 0 and heap[curr_id] < heap[parent_id]:
            self.swap(curr_id, parent_id, heap)
            curr_id = parent_id
            parent_id = (curr_id - 1) //2

    def peek(self):
        return self.heap[0]

    def pop(self):
        self.swap(0, len(self.heap)-1, self.heap)
        root_val = self.heap.pop()
        self._siftdown(0, len(self.heap) - 1, self.heap)
        return root_val

    def push(self, value):
        self.heap.append(value)
        self._siftup(len(self.heap) - 1, self.heap)

    def swap(self, i, j, heap):
        heap[i], heap[j] = heap[j], heap[i]


def validate_minHeap(mh):
    last_parent_id = (len(mh) -2)//2
    for i in reversed(range(last_parent_id)):
        c1 = i*2 + 1
        c2 = c1 + 1
        if c2 <= len(mh)-1 and mh[c2] < mh[c1]:
            min_child = mh[c2]
        else:
            min_child = mh[c1]
        if mh[i] > min_child:
            return False
    return True


if __name__ == "__main__":
    # array1 = [544, -578, 556, 713, -655, -359, -810, -731, 194,
    #           -531, -685, 689, -279, -738, 886, -54, -320, -500,
    #           738, 445, -401, 993, -753, 329, -396, -924, -975,
    #           376, 748, -356, 972, 459, 399, 669, -488, 568, -702,
    #           551, 763, -90, -249, -45, 452, -917, 394, 195, -877,
    #           153, 153, 788, 844, 867, 266, -739, 904, -154, -947,
    #           464, 343, -312, 150, -656, 528, 61, 94, -581]
    # mh1 = MinHeap(array1)
    # print(mh1.peek())
    # print(validate_minHeap(mh1.heap))
    # print(mh1.heap[7], mh1.heap[15])

    arr2 = [3,2,1,5,4,7,6,5]
    mh1 = MinHeap(arr2[:3+1])
    print(mh1.heap)
    print(arr2)
    mh1.pop()
    print(mh1.heap)
    print(arr2)
