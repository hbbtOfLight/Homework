a = "I am global variable!"


def enclosing_funcion():
    a = "I am variable from enclosed function!"

    def inner_function():
        # a = "I am local variable!"   # next two lines replace it for 2, 3
        # global a    # 2
        nonlocal a    # 3
        print(a)
    inner_function()   # 1


