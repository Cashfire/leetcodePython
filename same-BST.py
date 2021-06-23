# from BST import BST

def sameBsts(arrayOne, arrayTwo):
    return are_same_BST(arrayOne, arrayTwo, 0, 0, float('-inf'), float('inf'))


def are_same_BST(arr1, arr2, idx1, idx2, lower_bound, upper_bound):
    if idx1 == -1 or idx2 == -1:
        return idx1 == idx2
    if arr1[idx1] != arr2[idx2]:
        return False
    left1 = get_root_idx(arr1, idx1, lower_bound, left=True)
    left2 = get_root_idx(arr2, idx2, lower_bound, left=True)
    right1 = get_root_idx(arr1, idx1, upper_bound, left=False)
    right2 = get_root_idx(arr2, idx2, upper_bound, left=False)
    curr_root_val = arr1[idx1]
    left_the_same = are_same_BST(arr1, arr2, left1, left2, lower_bound, curr_root_val)
    right_the_same = are_same_BST(arr1, arr2, right1, right2, curr_root_val, upper_bound)
    return left_the_same and right_the_same



def get_root_idx(arr, old_root_idx, bound, left=True):
    old_root = arr[old_root_idx]
    for i in range(old_root_idx+1, len(arr)):
        if left:
            # find_root first smaller after parent_idx,
            # but still >= lower_bound
            if arr[i] < old_root and arr[i] >= bound:
                return i
        else:
            # find_root fist equal-or-greater after old_root_idx,
            # but still < upper_bound
            if arr[i] >= old_root and arr[i] < bound:
                return i
    return -1


if __name__ == "__main__":
    array1 = [10, 15, 8, 12, 94, 81, 5, 2, 11]
    array2 = [10, 8, 5, 15, 2, 12, 11, 94, 81]
    print(sameBsts(array1, array2))
    # print(get_root_idx(array1, 0, float('-inf'), left=True))
