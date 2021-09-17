import math


def ask_and_print_divs():
    val = int(input("Enter an integer value\n"))
    div_list = list()
    for i in range(1, int(math.sqrt(val)) + 1):
        if val % i == 0:
            div_list.append(i)
            div_list.append(int(val / i))
    if div_list[-1] == int(math.sqrt(val)):
        div_list.pop()
    div_list.sort()
    print(div_list)


ask_and_print_divs()
