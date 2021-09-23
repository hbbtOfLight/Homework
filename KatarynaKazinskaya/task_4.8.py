def get_pairs(arg_list: list):
    last = len(arg_list)
    if last < 2:
        return None
    second_idx = 1
    t_list = list()
    while second_idx < last:
        t_list.append((arg_list[second_idx - 1], arg_list[second_idx]))
        second_idx += 1
    return t_list


print(get_pairs([1, 2, 3, 8, 9]))
print(get_pairs(["need to", "sleep", "more"]))
print(get_pairs([1]))
