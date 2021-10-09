class MySquareIterator:
    def __init__(self, collection):
        self.collection = collection
        self.idx = 0

    def __next__(self):
        if self.idx >= len(self.collection):
            raise StopIteration
        res = self.collection[self.idx] ** 2
        self.idx += 1
        return res

    def __iter__(self):
        return self

