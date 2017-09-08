import time


def timer(func):
    def function_timer(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        return (end - start, func(*args, **kwargs))
    return function_timer
