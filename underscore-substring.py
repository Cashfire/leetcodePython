
def underscorifySubstring(string, substring):
    locs = get_indices(string, substring)
    print(locs)
    new_locs = collapse(locs)
    print(new_locs)
    return underscorify(string, new_locs)


def get_indices(string, substring):
    indices = [] #[inclusive_start_idx, nonclusive_end_idx]
    start_idx = 0
    while start_idx < len(string):
        nxt = string.find(substring, start_idx)
        if nxt == -1:
            break
        else:
            indices.append([nxt, nxt + len(substring)])
            start_idx = nxt + 1
    return indices


def collapse(indices):
    if not indices:
        return indices
    result = [indices[0]]
    prev = result[0]
    for i, curr in enumerate(indices):
        if curr[0] <= prev[1]:
            prev[1] = curr[1]
        else:
            result.append(curr)
        prev = result[-1]
    return result


def underscorify(string, indices):
    if not indices:
        return string
    new_str = []
    str_i = 0
    for idx in indices:
        new_str.append(string[str_i: idx[0]])
        new_str.append('_' + string[idx[0]: idx[1]] + '_')
        str_i = idx[1]
    new_str.append(string[str_i: ])
    print(new_str)
    return ''.join(new_str)



if __name__ == "__main__":
    string1 = "testthis is a testtest to see if testestest it works"
    substring1 = 'test'
    string2 = "ttttttttttttttbtttttctatawtatttttastvb"
    p = string2.index('b')
    substring2 = "ttt"
    string3 = "atttttb ttb"
    print(underscorifySubstring(string3, substring2))
