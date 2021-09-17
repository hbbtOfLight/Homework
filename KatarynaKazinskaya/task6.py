def turn_to_integer(t):
    num = 0
    for i in t:
        num *= 10
        num += i
    return num


print(turn_to_integer((1, 2, 3, 4, 5, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8)))
