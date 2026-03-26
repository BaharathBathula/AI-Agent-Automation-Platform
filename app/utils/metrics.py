import time


def track_execution(func):

    def wrapper(*args, **kwargs):
        start = time.time()

        result = func(*args, **kwargs)

        duration = time.time() - start
        print(f"[METRIC] {func.__name__} took {duration:.2f}s")

        return result

    return wrapper
