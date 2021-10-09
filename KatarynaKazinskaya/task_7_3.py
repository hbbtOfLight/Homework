import time
from contextlib import ContextDecorator


class LoggerDecorator(ContextDecorator):
    def __enter__(self):
        self.start_time = time.process_time_ns()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end_time = time.process_time_ns()
        if exc_val is not None:
            print("Exception happened! " + str(exc_val))
        print("Time: {0} ns ".format(self.end_time - self.start_time))
        return True


