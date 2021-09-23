def split_by_idxes(s, idx_list):
    if idx_list is None or len(idx_list) == 0:
        return [s]
    w_list = list()
    size = len(s)
    prev = 0
    for i, c in enumerate(idx_list):
        if size > c > -size - 1:
            w_list.append(s[prev:c])
            prev = c
    w_list.append(s[idx_list[-1]:])
    return w_list


s = "he is a cute anime boy he must suffer"
print(split_by_idxes(s, [4, 7, 10, -150, 15, -7]))
print(split_by_idxes(s, []))
print(split_by_idxes(s, [-100500]))

