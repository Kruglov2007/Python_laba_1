# Напишите декоратор log_calls, который записывает в файл время вызова, имя
# и аргументы вызванной функции. Один вызов функции - одна строка в файле.
# Декоратор должен принимать имя файла для записи в качестве параметра.
import time
import functools
def log_calls(filename):
    def decorator_calls(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result=func(*args, **kwargs)
            start_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
            arguments = f"args={args}, kwargs={kwargs}"
            with open(filename, "a", encoding="utf-8") as file:
                file.write(f"{start_time}: Функция: {func.__name__}; {arguments}\n")

            return result
        return wrapper
    return decorator_calls


LOG_FILE = "test.log"

@log_calls(LOG_FILE)
def calc_power(base, exponent=2):
    return base ** exponent

# Вызываем функцию с разными аргументами
calc_power(5)
calc_power(3, exponent=4)
calc_power(10, 3)

# Читаем и выводим созданный файл
with open(LOG_FILE, "r", encoding="utf-8") as f:
    print("--- Содержимое файла test.log ---")
    print(f.read())