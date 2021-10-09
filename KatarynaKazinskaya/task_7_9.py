class EvenRange:
    def __init__(self, fst, lst):
        if fst % 2:
            fst += 1
        self.fst = fst
        self.lst = lst

    def __iter__(self):
        return self

    def __next__(self):
        if self.fst >= self.lst:
            print("Out of number")
            raise StopIteration("Out of number")
        res = self.fst
        self.fst += 2
        return res
