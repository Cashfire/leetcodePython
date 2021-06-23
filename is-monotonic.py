
def is_monotonic(array):
    # very neat solution
    if len(array) <= 2:
        return True
    is_non_increasing = True
    is_non_decreasing = True
    for i in range(1, len(array)):
        n1, n2 = array[i-1], array[i]
        if n1 < n2:
            is_non_increasing = False
        if n1 > n2:
            is_non_decreasing = False
    return is_non_decreasing or is_non_increasing


def isMonotonic(array):
    # optimized to early stop
    if len(array) <= 2:
        return True
    main_direct = 0
    for i in range(1, len(array)):
        diff = array[i] - array[i-1]
        if diff == 0:
            continue
        if main_direct == 0:
            main_direct = diff
            continue
        if main_direct/diff < 0:
            return False
    return True




if __name__ == "__main__":
    arr1 = [0,1,-4,-5]
    print(is_monotonic(arr1))
    print(isMonotonic(arr1))
