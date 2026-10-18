# Напишите функцию unique_elements, которая принимает вложенный список и
# возвращает уникальные элементы.
# Пример:
# >> list_a = [1, 2, 3, [4, 3, 1], 5, [6, [7, [10], 8, [9, 2 ,3]]]]
# >> unique_elements(list_a)
# [1, 2, 3, 4, 5, 6, 7, 10, 8, 9]

import copy
def flatten_list(list_a):
    i=0
    while i<len(list_a):
        if type(list_a[i]) is list:
            flatten_list(list_a[i])
            list_a[i:i+1] = list_a[i]
            
        else:
            i+=1

def unique_elements(list_a):
    list_copy = copy.deepcopy(list_a) 
    flatten_list(list_copy)
    result=list(dict.fromkeys(list_copy))
    return result

list_a = [1, 2, 3, [4, 3, 1], 5, [6, [7, [10], 8, [9, 2 ,3]]]]
print(unique_elements(list_a))
