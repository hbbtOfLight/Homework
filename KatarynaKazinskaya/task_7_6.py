from math import sqrt
from itertools import islice, count
from task_7_5 import checker, EvenException, LessThan2Exception
def is_prime(num):
    return all(num % i for i in islice(count(2), int(sqrt(num) - 1)))


def is_goldbachs(num):
    for i in islice(count(2), num//2 - 1):
        if is_prime(i) and is_prime(num - i):
            return True
    return False


while(True):
    number = input("Enter an even number > 2. Press q to exit")
    if number == 'q':
        break
    try:
        checker(int(number))
    except EvenException:
        print("Do not work for odd numbers")
    except LessThan2Exception:
        print("Doesn't work for numbers <= 2")
    else:
        try:
            print("For this number Goldbach is right ? : {0}".format(is_goldbachs(int(number))))
        except Exception:
            print("Unknown exception")