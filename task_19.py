# Напишите декоратор cache, который кэширует результат вызова функции
# (сохраняет в словаре). Когда функция вызывается снова с теми же аргументами,
# декоратор должен возвращать результат из кэша, вместо того, чтобы вызывать
# декорированную функцию.
import functools
def cache(func):
    cache = {}
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
         key = (args, frozenset(kwargs.items()))
         if key in cache:
              return cache[key]
         result=func(*args, **kwargs)
         cache[key]=result
         return result
    return wrapper


        
