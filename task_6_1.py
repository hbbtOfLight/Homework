class Counter:
    def __init__(self, start=0, end=float("+inf")):
        self.start = start
        self.end = end

    def increment(self):
        if self.start >= self.end:
            raise IncrementException("Maximal value is reached.")
        else:
            self.start += 1

    def get(self):
        return self.start


class IncrementException(Exception):
    pass


c = Counter(start=43, end=44)
c.increment()
c.increment()
print(c.get())
