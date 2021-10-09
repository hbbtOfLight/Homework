from collections.abc import Iterable


class MyNumberCollection:
    def __init__(self, start, end=None, step=None):
        self.lst = list()
        if isinstance(start, Iterable):
            for i in start:
                if type(i) not in (int, float):
                    raise TypeError("MyNumberCollection supports only numbers!")
                self.lst.append(i)

        elif type(start) in(int, float) and type(end) in(int, float) and type(step) is int:
            self.lst = list(range(start, end, step))

        else:
            raise TypeError("MyNumberCollection supports only numbers!")

    def __iter__(self):
        return self.lst.__iter__()

    def __getitem__(self, item):
        return self.lst[item] ** 2

    def append(self, item):
        if type(item) not in (int, float):
            raise TypeError(f'{type(item)} is not number!')
        self.lst.append(item)

    def __add__(self, other):
        return MyNumberCollection(self.lst + other.lst)

    def __str__(self):
        return str(self.lst)


col1 = MyNumberCollection(0, 5, 2)
print(col1)
col2 = MyNumberCollection((1,2,3,4,5))
print(col2)
col1.append(7)
print(col1)
print(col1 + col2)
print(col2[4])
for item in col1:
    print(item)




