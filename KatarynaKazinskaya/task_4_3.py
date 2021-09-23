# implement for none


def split(s, sep=None, maxsplit=-1):
    w_list = list()
    prev_idx = -1
    count = 0
    curr = 0
    s_size = len(s)
    if sep is not None:
        sep_size = len(sep)
        while curr <= s_size:
            if curr == s_size or s[curr: curr + sep_size] == sep:
                w_list.append(s[prev_idx + 1: curr])
                curr += sep_size
                prev_idx = curr - 1
                count += 1
                if count == maxsplit != -1:
                    w_list.append(s[curr:])
                    return w_list
            else:
                curr += 1
    if sep is None:
        while curr < s_size:
            while curr < s_size and s[curr] == ' ':
                curr += 1
            curr1 = curr
            if count == maxsplit > -1:
                w_list.append(s[curr:])
                return w_list
            while curr1 < s_size and s[curr1] != ' ':
                curr1 += 1
            w_list.append(s[curr:curr1])
            count += 1
            curr = curr1
    return w_list


print(split("123<>123<>123<>123", "<>"))
print(split("muahaha   ahaha   ahahh a ha a  hah"))
print(split('', 'b'))
print(split(''))

