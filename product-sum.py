
def productSum(array):
	return productSum_helper(array, 1)


def productSum_helper(array, d):
	result = 0
	for x in array:
		if isinstance(x, int):
			result +=  x
		else:
			result += productSum_helper(x, d+1)
	return result * d


def productSum_iterative(array):
    depth = 1
    result = 0
    str_arr = str(array)[1:]
    for x in str_arr:
        if type(x) == int:
            result += depth * x
        elif x == '[':
            depth += 1
        elif x == ']':
            depth -= 1
    return result


if __name__ == '__main__':
    arr = [5,2,[7,-1], 3, [6, [-13, 8]], 4]
    arr2 = [5, 2, [7, -1], 3, [6, [-13, 8], 4]]
    # print(productSum(arr2))

    # print(productSum_iterative(arr2))
    # print("-5".isnumeric())
    for i in str(arr2):
        print(i)
