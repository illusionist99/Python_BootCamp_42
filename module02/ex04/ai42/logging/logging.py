import time

# @log is just an easier way of saying a = log(func)

def log(func):

    def wrapper(*args):
        f = open("machine.log", "a")
        start_time = time.time()
        if callable(func):
            func(*args)
        f.write(f'(cmaxime)Running: {func.__name__:<8} [ exec-time = {func.__name__} ]\n')
        f.close()
    return wrapper
