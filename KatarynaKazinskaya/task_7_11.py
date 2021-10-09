def endless_fib_generator():
    def inner_generator(seed1=1, seed2=0):
           while True:
               yield seed1
               seed1 += seed2
               seed2 = seed1 - seed2

    return inner_generator()
