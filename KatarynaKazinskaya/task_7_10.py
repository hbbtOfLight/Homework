def endless_generator():
    def inner_generator(seed=-1):
        while True:
            seed += 2
            yield seed
    return inner_generator()
