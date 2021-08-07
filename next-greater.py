"""
Given an array of integer, for each integer find the next greater number after it with circular
"""
def nextGreaterElement(array):
    # O(n) time
    result = [-1] * len(array)
    stack = [0]
    for i in range(1, 2 * len(array)):
        circle_i = i % len(array)
        while len(stack) > 0:
            if circle_i == stack[-1]:
                return result
            if array[circle_i] > array[stack[-1]]:
                result[stack.pop()] = array[circle_i]
            else:
                break
        stack.append(circle_i)
    return result

if __name__ == "__main__":
    array1 = [2, 5, -3, -4, 6, 7, 2]
    array3 = [5, 6, 6, 6, 7, -1, 5]
    array2 = [7,5,6,4]
    print(nextGreaterElement(array1))
