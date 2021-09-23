def foo(arg_list):
    prod = 1
    zero_count = 0
    for i in arg_list:
        if i == 0:
            zero_count += 1
        else:
            prod *= i
    if zero_count > 1:
        prod = 0
    newarr_lmbd = lambda i: 0 if zero_count > 0 and i != 0 else prod // i if i != 0 else prod
    return [newarr_lmbd(i) for i in arg_list]


print(foo([1, 2, 0, 5]))
print(foo([10, 3, 25, 4, -1]))
