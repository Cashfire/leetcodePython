

def longest_peak(array):
    longest = 0
    i = 1
    while i < len(array)-1:
        is_peak = array[i-1] < array[i] and array[i] > array[i+1]
        if not is_peak:
            i += 1
            continue

        l = i - 2
        while l >= 0 and array[l] < array[l + 1]:
            l -= 1

        r = i + 2
        while r < len(array) and array[r] < array[r - 1]:
            r += 1

        curr_len = r - l - 1
        longest = max(longest, curr_len)
        i = r
    return longest

def longestPeak(array):
    prev_diff = (array[1] - array[0])
    longest_peak = 0
    peak_counting = False
    curr_len = 0
    if prev_diff > 0:
        curr_len = 2
        peak_counting = True
    for i in range(2, len(array)):
        curr_diff = (array[i] - array[i-1])
        if curr_diff == 0:
            if peak_counting and prev_diff < 0:
                longest_peak = max(longest_peak, curr_len)
            curr_len = 0
            peak_counting = False
        elif curr_diff > 0:
            if prev_diff < 0:
                if peak_counting:
                    longest_peak = max(longest_peak, curr_len)
                curr_len = 2
            elif prev_diff == 0:
                curr_len = 2
            else:
                curr_len += 1
            peak_counting = True
        else:
            if peak_counting:
                curr_len += 1
        print('i=', i, ' ,num=', array[i],' ,curr_len =',curr_len)
        prev_diff = curr_diff
    if peak_counting and prev_diff < 0:
        longest_peak = max(longest_peak, curr_len)
    return longest_peak



if __name__ == "__main__":
    arr1 = [1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]
    ans1 = 6
    arr2 = [1, 2, 3, 4, 5, 1]
    ans2 = 6
    arr3 = [1,3,2]
    ans3 = 3
    arr4 = [5, 4, 3, 2, 1, 2, 10, 12]
    ans4 = 0
    print(longest_peak(arr3))
