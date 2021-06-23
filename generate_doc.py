"""
If you're given characters = 'abcabc, and the document = "aabbccc",
then you cannot generate the document because you're missing one c.
Note: your can always generate the empty string ""
"""


def generate_document(characters, document):
    # O(n+m) time, n = len(characters), m = len(document)
    #O(c) space, c = len(unique(characters))
    if document == "":
        return True
    char_dict = get_char_dict(characters)
    for c in document:
        count = char_dict.get(c)
        if count is None:
            return False
        count -= 1
        if count < 0:
            return False
        char_dict[c] = count
    return True


def get_char_dict(characters):
    result = {}
    for c in characters:
        # count = result.get(c)
        # if count is None:
        #     result[c] = 1
        # else:
        #     result[c] += count + 1
        if result.get(c) is None:
            result[c] = 0
        result[c] += 1
    return result




if __name__ == "__main__":
    characters1 = "Bste!hetsi ogEAxpelrt x "
    document1 = "AlgoExpert is the Best!"
    print(generate_document(characters1, document1))



