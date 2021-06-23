# Do not edit the class below except for
# the push method. Feel free to add new
# properties and methods to the class.
class ContinuousMedianHandler:
    def __init__(self):
        # Write your code here.
        self.median = None
        self.lowers = Heap(max_heap_func)
        self.greaters = Heap(min_heap_func)

    def insert(self, number):
        if not self.lowers.length or self.lowers.peek() > number:
            self.lowers.push(number)
        else:
            self.greaters.push(number)
        self.rebalance_heaps()
        self.update_median()

    def rebalance_heaps(self):
        if self.lowers.length - self.greaters.length == 2:
            self.greaters.push(self.lowers.pop())
        elif self.greaters.length - self.lowers.length == 2:
            self.lowers.push(self.greaters.pop())

    def update_median(self):
        if self.lowers.length == self.greaters.length:
            self.median = (self.lowers.peek() + self.greaters.peek())/2
        elif self.lowers.length > self.greaters.length:
            self.median = self.lowers.peek()
        else:
            self.median = self.greaters.peek()

    def getMedian(self):
        return self.median



class Heap:
    def __init__(self, compare_func):
        self.compare_func = compare_func
        self.heap = []
        self.length = len(self.heap)

    def push(self, value):
        self.heap.append(value)
        self.length += 1
        self._shiftup(self.length - 1, self.heap)

    def _shiftup(self, idx, heap):
        parent_idx = (idx - 1)//2
        while parent_idx >= 0 and self.compare_func(heap[idx],heap[parent_idx]):
            self.swap(idx, parent_idx, heap)
            idx = parent_idx
            parent_idx = (idx - 1)//2

    def peek(self):
        return self.heap[0]

    def swap(self, i, j, heap):
        heap[i], heap[j] = heap[j], heap[i]

    def pop(self):
        self.swap(0, self.length - 1, self.heap)
        self.length -= 1
        self._shiftdown(0, self.length - 1, self.heap)
        return self.heap.pop()

    def _shiftdown(self, curr_idx, end_idx, heap):
        left_idx = curr_idx * 2 + 1
        while left_idx <= end_idx:
            right_idx = left_idx + 1 if left_idx + 1 <= end_idx else None
            if right_idx is not None and self.compare_func(heap[right_idx], heap[left_idx]):
                id_to_swap = right_idx
            else:
                id_to_swap = left_idx
            if self.compare_func(heap[id_to_swap], heap[curr_idx]):
                self.swap(id_to_swap, curr_idx, heap)
                curr_idx = id_to_swap
                left_idx = curr_idx * 2 + 1
            else:
                return


def max_heap_func(a, b):
    return a > b


def min_heap_func(a, b):
    return a < b


if __name__ == "__main__":
    median_finder1 = ContinuousMedianHandler()
    median_finder1.insert(5)
    median_finder1.insert(10)
    median_finder1.insert(100)
    # print(median_finder1.getMedian())
    median_finder1.insert(200)
    # print(median_finder1.getMedian())
    # print(median_finder1.lowers.heap)
    # print(median_finder1.greaters.heap)

    arr2 = [5, 10, 100, 200, 6, 13, 14, 50, 51, 52, 1000, 10000, 10001]
    median_finder2 = ContinuousMedianHandler()
    for num in arr2:
        median_finder2.insert(num)
        # print("after inserting ", num)
        # print(median_finder2.lowers.heap)
        # print(median_finder2.greaters.heap)
    print(median_finder2.getMedian())
