# Напишите декоратор @timing, который выводит на экран время выполнения
# функции в миллисекундах.
import functools
import time
def timing(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        time_start=time.perf_counter()
        result=func(*args, **kwargs)
        time_end=time.perf_counter()
        print(f"Время выполнения в мс: {(time_end-time_start)*1000}")
        return result
    return wrapper

@timing
def proisv(a,b):
    return a*b

proisv(13, 49)
