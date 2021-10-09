class CustomBaseException(Exception):
    pass


class EvenException(CustomBaseException):
    pass


class LessThan2Exception(CustomBaseException):
    pass


def check_even(num):
    if num % 2 == 1:
        raise EvenException


def check_gt2(num):
    if num < 2:
        raise LessThan2Exception


def checker(num):
    try:
        check_even(num)
        check_gt2(num)
    except EvenException:
        raise
    except LessThan2Exception:
        raise
