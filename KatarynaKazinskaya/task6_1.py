import math


def pretty_print(arg_list):
    arg_list.append(1)
    arg_list.sort()
    max_space = (int(math.log10(arg_list[-1])) + 1) * 2
    for idx, i in enumerate(arg_list):
        values = list()
        skillet = ""
        for j in arg_list[1:]:
            skillet += '{:' + str(-max_space) + '}'
            values.append(i * j)
        if idx == 0:
            print(('{:' + str(max_space) + '}').format(' ') + skillet.format(*values))
        else:
            print(('{:' + str(max_space) + '}').format(i) + skillet.format(*values))


pretty_print([1, 2, 1001, 10000011])