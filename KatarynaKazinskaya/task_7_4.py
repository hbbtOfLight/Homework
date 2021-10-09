import collections.abc


def dict_exception_handler(exception_dict):
    def func_caller(func):
        def exception_handler(*args, **kwargs):
            try:
                func(*args, **kwargs)
            except Exception as e:
                if type(e) in exception_dict:
                    arg = exception_dict[type(e)]
                    if isinstance(arg, collections.abc.Callable):
                        print(str(e) + " " + str(exception_dict[type(e)]()))
                    else:
                        print(str(e) + " " + str(exception_dict[type(e)]))
                else:
                    print("Unknown Exception!")
            else:
                print("Ok")

        return exception_handler
    return func_caller



