import math


def get_digits(n: int):
    t = list()
    digs = 10 ** int(math.log10(n))
    while n != 0:
        t.append(n//digs)
        n -= t[-1] * digs
        digs //= 10
    return tuple(t)


print(get_digits(1234567891011))

