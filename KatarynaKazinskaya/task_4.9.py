import string


def test_1_1(*strings):
    if len(strings) == 0:
        return []
    f_char_list = set(strings[0])
    char_list = set(strings[0])
    for c in f_char_list:
        for word in strings[1:]:
            if c not in word:
                char_list.remove(c)
                break
    return char_list


def test_1_2(*strings):
    char_set = set()
    for i in strings:
        for j in i:
            char_set.add(j)
    return char_set


def test_1_4(*strings):
    lower_alphabet = set(string.ascii_lowercase)
    for s in strings:
        for c in s.lower():
            if c in lower_alphabet:
                lower_alphabet.remove(c)
    return lower_alphabet


def test_1_3(*strings):
    char_set = set()
    ones_set = set()
    for s in strings:
        for j in s:
            if j in char_set:
                continue
            elif j in ones_set:
                char_set.add(j)
            else:
                ones_set.add(j)
    return char_set







test_strings = ["hello", "world", "python", ]
print(test_1_1(*test_strings))
print(test_1_2(*test_strings))
print(test_1_4(*test_strings))
print(test_1_3(*test_strings))
