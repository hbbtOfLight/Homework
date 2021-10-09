class FileOpener:
    def __init__(self, filepath, mode):
        self.path = filepath
        self.mode = mode

    def __enter__(self):
        self.file = open(self.path, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            print("Exception: " + str(exc_val))
        self.file.close()
        return True

