"""
run-length encoding is a form of lossless data compression, in which data are stored
as a single data value and its count. The "AAA" would be run-length-encoded to "3A".
However, when data is more complicated and contain all sort of special characters,
including numbers. "12A" can be decoded to either "AAAAAAAAAAAA" or "1AA".
Thus, long runs (>= 10 characters) should be encode in a split fashion,
like "AAAAAAAAAAAA" should be encoded to "9A3A"
like "1  222 333    444  555" to "112 321 334 342 35"
llike "1A2BB3CCC4DDDD" to "111A122B133C144D"
"""


def runLengthEncoding(string):
    result = ""
    count = 1
    prev = string[0]
    for i in range(1, len(string)):
        curr = string[i]
        if curr == prev:
            count += 1
        else:
            result += split_long_run(count, prev)
            prev = curr
            count = 1
    # handle the last run
    result += split_long_run(count, prev)
    return result


def split_long_run(count, prev):
    result = ""
    if count <= 9:
        result += str(count)+prev
    else:
        n = count//9
        m = count%9
        result += ("9"+prev)*n + str(m) + prev
    return result


def run_length_encode(string):
    result = []
    count = 1
    for i in range(1, len(string)):
        curr = string[i]
        prev = string[i-1]
        if curr != prev or count == 9:
            result.append(str(count))
            result.append(prev)
            count = 0
        count += 1
    # handle the last run
    result.append(str(count))
    result.append(string[-1])
    return "".join(result)


if __name__ == "__main__":
    arr1 = "AAAAAAAAAAAAABBCCCCDD"
    print(run_length_encode(arr1) == "9A4A2B4C2D")
    arr2 =  "1  222 333    444  555"
    ans2 = "112 321 334 342 35"
    arr3 =  "1A2BB3CCC4DDDD"
    ans3 = "111A122B133C144D"
    arr4 = " "*26
    ans4 = "9 9 8 "
    print(runLengthEncoding(arr2) == ans2)
    print(runLengthEncoding(arr3) == ans3)
    print(runLengthEncoding(arr4) == ans4)
