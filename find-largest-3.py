
def findThreeLargestNumbers(array):
    largest3 = sorted(array[:3])
    for i in range(3, len(array)):
        rerange(largest3, array[i])
    return largest3


def rerange(arr3, num):
    # L1 >= L2 >= L3
    L3, L2, L1 = arr3
    if num <= L3:
        return
    if num >= L1:
        # arr3 = [L2, L1, num]
        arr3[0] = L2
        arr3[1] = L1
        arr3[2] = num
    elif num >= L2:
        # arr3 = [L2, num, L1]
        arr3[1] = num
        arr3[0] = L2
    else:
        # arr3 = [num, L1, L2]
        arr3[0] = num



if __name__ == "__main__":
    my_arr = [141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]
    my_list = [55, 7, 8, 3, 43, 11]
    print(findThreeLargestNumbers(my_list))

