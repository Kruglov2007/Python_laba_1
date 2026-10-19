# Напишите функцию, которая производит слияние двух словарей. Используйте
# рекурсию. В обоих словарях может быть любой уровень вложенности. Вложены
# могут быть другие коллекции: словари, списки, множества, кортежи.
# Пример:
# >> dict_a = {“a”: 1, “b”: {“c”: 1, “f”: 4}}
# >> dict_b = {“d”: 1, “b”: {“c”: 2, “e”: 3}}
# >> merge_dicts(dict_a, dict_b)
# >> print(dict_a)
# {“a”: 1, “b”: {“c”: 2, “e”: 3, “f”: 4}, “d”: 1}
def merge_dicts(dict_a, dict_b):
    for key, value in dict_b.items():
         if key in dict_a:
            type_a = type(dict_a[key])
            type_b = type(value)
            if type_a  is dict and type_b is dict:
                merge_dicts(dict_a[key], value)
            elif (type_a is list and type_b is list) or (type_a is tuple and type_b is tuple):
                    dict_a[key] = dict_a[key] + value
            elif type_a is set and type_b is set:
                    dict_a[key] = dict_a[key] | value
            else:
                dict_a[key] = deep_copy(value)
         else:
               dict_a[key] = deep_copy(value)
def deep_copy(obj):
    """Вспомогательная функция для безопасного копирования коллекций 
    любой вложенности без использования сторонних библиотек и isinstance"""
    t = type(obj)
    if t is dict:
        return {k: deep_copy(v) for k, v in obj.items()}
    elif t is list:
        return [deep_copy(x) for x in obj]
    elif t is set:
        return {deep_copy(x) for x in obj}
    elif t is tuple:
        return tuple(deep_copy(x) for x in obj)
    return obj


dict_a = {"a": 1, "b": {"c": 1, "f": 4}}
dict_b = {"d": 1, "b": {"c": 2, "e": 3}}

merge_dicts(dict_a, dict_b)
print(dict_a)

