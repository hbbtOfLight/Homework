from contextlib import contextmanager


@contextmanager
def FileOpener(filepath, mode):
    file = None
    try:
        file = open(filepath, mode)
    except FileNotFoundError:
        print("File not found!")
    except ValueError:
        print("Value error!")
    finally:
        try:
            yield
        except Exception:
            print("Exception occured!")
    if file is not None:
        file.close()



