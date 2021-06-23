
class SortAlgos:
    def quick_sort(self):
        pass

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

if __name__ == "__main__":
    A = [3, 6, 9, 4, 2]
    arr2 = [8, 5, 2, 9, 5, 6, 3]
    # SortAlgos().bubble_sort_brute_force(A)
    selection_sort(A)
    print(A)
