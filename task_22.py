# Напишите декоратор @type_check, который проверяет, что параметры
# функции соответствуют указанным типам. Если нет - выбрасывает
# исключение TypeError.
import functools

def type_check(*dec_args, **dec_kwargs):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if len(args) != len(dec_args):
                raise TypeError("Не соответствие указанных типов")
            
            
            for i in range(len(args)):
                if type(args[i]) is not dec_args[i]:
                    raise TypeError("Не соответствие указанных типов")
            
            for key in kwargs:
                # Если передан аргумент, тип которого не описан в декораторе,
                # или если тип не совпадает — выбрасываем исключение
                if key not in dec_kwargs or type(kwargs[key]) is not dec_kwargs[key]:
                    raise TypeError("Не соответствие указанных типов")
                                    
            return func(*args, **kwargs)
        return wrapper
    return decorator

# --- Проверка работы ---
@type_check(int, str)
def example(a, b):
     print(f"{a} and {b}")

example(13, "nan")  # Выведет: 13 and nan

