
class SortAlgos:
    def quick_sort(self, arr, k,  l=None, r=None):
    # O(NlogN) time and O(logN) space
        if l is None:
            l, r = 0, len(arr) -1
        if l >= r:
            return
        j = self.partition(arr, l, r)
        self.quick_sort(arr,k, l, j - 1)
        self.quick_sort(arr,k, j + 1, r)

    def partition(self,arr, l, r):
        pivot = arr[l]
        i, j = l+1, r
        while i <= j:
            while arr[i] <= pivot:
                if i == r:
                    break
                i += 1
            while arr[j] >= pivot:
                if j == l:
                    break
                j -= 1
            if i >= j:
                break
            self.__swap(i, j, arr)
        self.__swap(l, j, arr)
        return j

    def quick3way(self, arr, l=None, r=None):
        # good if array has lots of duplicates element
        if l is None:
            l, r = 0, len(arr) -1
        if r <= l:
            return
        pivot = arr[l]
        p1, p2 = l, r
        i = l + 1
        while i <= p2:
            if arr[i] < pivot:
                self.__swap(i, p1, arr)
                p1 += 1
                i += 1
            elif arr[i] > pivot:
                self.__swap(i, p2, arr)
                p2 -= 1
            else:
                i += 1
        self.quick3way(arr, l, p1 -1)
        self.quick3way(arr, p2 + 1, r)

    # def quick3way(self, array):

    def __swap(self, i, j, array):
        temp = array[j]
        array[j] = array[i]
        array[i] = temp

    def bubble_sort_brute_force(self, array):
        # O(n^2) time and O(1)
        # The 1st itr will put the largest to the last pos
        # the 2nd itr will put the 2nd-largest to the 2nd last pos
        n = len(array)
        for i in range(n -1):
            print('i=',i)
            for j in range(0, n - i - 1):
                if array[j] > array[j + 1]:
                    self.__swap(j, j + 1, array)
                self.__print_array(array, j)

    def __print_array(self,array, j):
        result = ""
        for i in range(len(array)):
            num = str(array[i])
            if i == j:
                result += "|" + num + ", "
            elif i == j + 1:
                result += num + "|, "
            else:
                result += num + ", "
        print(result)

    def bubble_sort(self, array):
        # n-1 passes, each pass (n-1-i) swaps, so O(n^2) time
        n = len(array)
        for i in range(0, n-1):
            is_sorted = True
            for j in range(0, n-1 - i):
                if array[j] > array[j+1]:
                    self.__swap(j, j+1, array)
                    is_sorted = False
            if is_sorted:
                break

    def insertion_sort1(self,array):
        # push arr[i] to before portion, which is already sorted
        n = len(array)
        for i in range(1, n):
            print('i = ',i)
            j = i
            key = array[i]
            while j > 0 and key < array[j-1]:
                array[j] = array[j-1]
                j -= 1
                self.__print_array(array,j-1)
            array[j] = key
            self.__print_array(array,j-1)
        return array


def insertion_sort(array):
    for i in range(1, len(array)):
        j = i
        key = array[i]
        while j > 0 and key < array[j - 1]:
            array[j] = array[j - 1]
            j -= 1
        array[j] = key
    return array


def selection_sort(array):
    # for each i, find_root min of the rest, and swap arr[i] and min
    n = len(array)
    for i in range(n-1):
        min_id = i
        for j in range(i+1, n):
            if array[j] < array[min_id]:
                min_id = j
        temp = array[i]
        array[i] = array[min_id]
        array[min_id] = temp
    return array


def quickselect(array, k):
    # O(n) time and O(1) space. time worst O(n^2)
    return qs_helper(array, 0, len(array) - 1, k-1)


def qs_helper(arr, l, r, k):
    while True:
        pivot = arr[l]
        i, j = l + 1, r
        while i <= j:
            while arr[i] <= pivot and i < r:
                i += 1
            while arr[j] >= pivot and j > l:
                j -= 1
            if i >= j:
                break
            swap(i, j, arr)

        swap(l, j, arr)
        if j == k:
            return arr[j]
        elif j < k:
            l = j + 1
        else:
            r = j - 1


def swap(i, j, arr):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

def quick3way(arr, l=None, r=None):
    # good if array has lots of duplicates element
    if l is None:
        l, r = 0, len(arr) -1
    if r <= l:
        return
    pivot = arr[l]
    p1, p2 = l, r
    i = l + 1
    while i <= p2:
        if arr[i] < pivot:
            swap(i, p1, arr)
            p1 += 1
            i += 1
        elif arr[i] > pivot:
            swap(i, p2, arr)
            p2 -= 1
        else:
            i += 1
    quick3way(arr, l, p1 -1)
    quick3way(arr, p2 + 1, r)


if __name__ == "__main__":
    A = [3, 6, 9, 4, 2]
    arr2 = [8, 5, 3, 9, 5, 6, 2]
    arr3 = [43, 42, 37]
    # SortAlgos().bubble_sort_brute_force(A)
    # selection_sort(A)
    # print(A)

    # SortAlgos().quick_sort(arr3, 1)
    # print(arr3)

    result = quickselect(arr3, 1)
    print(result)
