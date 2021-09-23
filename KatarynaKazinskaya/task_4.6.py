def find_longest_word(s: str) -> str:
    def is_delim(c):
        return c == '\n' or c == '\t' or c == ' ' or c == '\r'

    min = 0
    max = 0
    curr_min = 0
    curr_max = 0
    maxlen = -1
    for i in range(len(s) + 1):
        while i < len(s) and is_delim(s[i]):
            i += 1
        curr_min = i
        while i < len(s) and not is_delim(s[i]):
            i += 1
        curr_max = i
        if curr_max - curr_min > maxlen:
            max = curr_max
            min = curr_min
            maxlen = curr_max - curr_min
    return s[min:max]


print(find_longest_word('1  1  11   '))
