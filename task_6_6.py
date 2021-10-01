class Singleton:
    sun = None

    def __new__(cls, *args, **kwargs):
        if cls.sun is None:
            cls.sun = object.__new__(cls)
        return cls.sun





