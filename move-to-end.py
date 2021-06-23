


def moveElementToEnd(array, toMove):
    to_fill_id = 0
    for i in range(len(array)):
        if array[i] != toMove:
            array[to_fill_id] = array[i]
            to_fill_id += 1
    while to_fill_id <= len(array) - 1:
        array[to_fill_id] = toMove
        to_fill_id += 1
    return array


def move_element_to_end(array, toMove):
    i = 0
    j = len(array) - 1
    while i < j:
        while array[i] != toMove and i < j:
            i += 1
        while array[j] == toMove and j > i:
            j -= 1
        if array[i] == toMove:
            array[j], array[i] = array[i], array[j]
    return array


if __name__ == "__main__":
    arr = [3, 1, 2, 4, 5]
    num = 3
    print(move_element_to_end(arr, num))
