import time


def timer(func):
    def function_timer(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        return end - start
    return function_timer
