import functools


@functools.total_ordering
class Money:
    exchange_rate = {
        "USD": 1,
        "EUR": 0.8548,
        "BYN": 2.4939,
        "RUB": 72.5688,
        "UAN": 26.624,
        "PLN": 3.9288,
        "GBP": 0.73,
        "CNY": 6.4626,
        "JPY": 110.9373,

    }

    def __init__(self, val, currency="USD"):
        if currency.strip() not in Money.exchange_rate:
            raise AttributeError("No such currency")
        self.currency = currency.strip()
        self.val = val

    def __lt__(self, other):
        return self.val / Money.exchange_rate[self.currency] < other.val / Money.exchange_rate[other.currency]

    def __eq__(self, other):
        return self.val / Money.exchange_rate[self.currency] == other.val / Money.exchange_rate[other.currency]

    def __add__(self, other):
        add_val = other.val
        if other.currency != self.currency:
            add_val = add_val * Money.exchange_rate[self.currency] / Money.exchange_rate[other.currency]
        return Money(self.val + add_val, self.currency)

    def __radd__(self, other):  #zero add for sum(list())
        if other != 0:
            raise ArithmeticError("Can't add Money to argument")
        return Money(self.val, self.currency)

    def __sub__(self, other):
        sub_val = other.val
        if other.currency != self.currency:
            sub_val *= (Money.exchange_rate[self.currency] / Money.exchange_rate[other.currency])
        return Money(self.val + sub_val, self.currency)

    def __mul__(self, other: float):
        return Money(self.val * other, self.currency)

    def __rmul__(self, other: float):
        return Money(self.val * other, self.currency)

    def __divmod__(self, other):
        return Money(self.val / other, self.currency)

    def __str__(self):
        return f'{self.val:.2f} {self.currency}'


x = Money(10, "BYN")
y = Money(11)
z = Money(12.34, "EUR")
print(y + x)
print(3.11 * x + z + y * 0.8)
lst = [Money(10, "BYN"), Money(11), Money(12.01, "JPY")]
s = sum(lst)
print(s)  # result in “BYN”
