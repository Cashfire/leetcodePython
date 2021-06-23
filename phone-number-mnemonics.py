def get_digit_dict():
    result = {}
    for i in range(2):
        result[str(i)] = [str(i)]
    code = 97
    for i in range(2, 10):
        if i == 7 or i == 9:
            n = 4
        else:
            n = 3
        result[str(i)] = []
        for j in range(n):
            result[str(i)].append(chr(code))
            code += 1
    return result


def phone_number_remember(number_string):
    count = 0
    # O(4^(n+1)/(4-1)-1) time and O(4^n) space
    result = [[]]
    digit_dict = get_digit_dict()

    for d in number_string:
        chars = digit_dict.get(d)
        n = len(result)
        while n > 0:
            n -= 1
            sub = result.pop(0)
            for c in chars:
                count += 1
                result.append(sub+[c])
    for i in range(len(result)):
        result[i] = "".join(result[i])
    return result, count


def phone_remember_rec(phone_number):
    curr = ['0'] * len(phone_number)
    found = []
    phone_remember_helper(0, phone_number, curr, found)
    return found


def phone_remember_helper(i, phone_number, curr, found):
    if i == len(phone_number):
        result = "".join(curr)
        found.append(result)
    else:
        digit = phone_number[i]
        letters = get_digit_dict().get(digit)
        for letter in letters:
            curr[i] = letter
            phone_remember_helper(i+1, phone_number, curr, found)


if __name__ == "__main__":
    # dict1 = get_digit_dict()
    # print(dict1.get("7"))
    # my_result, run_times = phone_number_remember('6225854523')
    # print(len(my_result))
    # print(run_times, ' v.s. ', ((3**11)-1)/2 )
    print(phone_remember_rec('23'))
