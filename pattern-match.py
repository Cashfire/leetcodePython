

def patternMatcher(pattern, string):
    ptn_ls = list(pattern)
    counts = pattern_counts(ptn_ls)
    n = len(string)
    x_n = counts['x']
    y_n = counts['y']
    max_x_len = (n - y_n * 1) // x_n
    for x_len in range(1, max_x_len + 1):
        total_y_len = (n - x_len * x_n)
        if total_y_len % y_n == 0:
            y_len = total_y_len // y_n
            ptn_lens = {'x': x_len, 'y': y_len}
            result = match(ptn_lens, pattern, string)
            if result:
                return result
        else:
            continue
    return []


def match(ptn_lens, pattern, string):
    ptn_i = 0
    str_i = 0
    mapping = {}
    while str_i < len(string):
        p =  pattern[ptn_i]
        str_nxt = str_i + ptn_lens[p]
        if p not in mapping:
            mapping[p] = string[str_i : str_nxt]
            ptn_i += 1
            str_i = str_nxt
        else:
            if mapping[p] != string[str_i: str_nxt]:
                return []
            else:
                ptn_i += 1
                str_i = str_nxt
    return [mapping['x'], mapping['y']]


def pattern_counts(ptn_ls):
    counts = {}
    for p in ptn_ls:
        if p in counts:
            counts[p] += 1
        else:
            counts[p] = 1
    return counts

if __name__ == "__main__":
    string1 = 'abab'
    pattern1 = 'xyxy'
    # ptn_lens1 = {'x': 1, 'y':1}
    # print(match(ptn_lens1, pattern1, string1))
    ls = []
    if ls:
        print("A")
