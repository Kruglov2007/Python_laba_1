# Напишите функцию, которая принимает список и делает его “плоским”.
# Используйте рекурсию. Функция должна модифицировать переданный список, а не
# создавать новый.
# Пример:
# >> list_a = [1, 2, 3, [4], 5, [6, [7, [], 8, [9]]]]
# >> flatten_list(list_a)
# >> print(list_a)
# [1, 2, 3, 4, 5, 6, 7, 8, 9]
def flatten_list(list_a):
    i=0
    while i<len(list_a):
        if type(list_a[i]) is list:
            flatten_list(list_a[i])
            list_a[i:i+1] = list_a[i]
            
        else:
            i+=1

list_a = [1, 2, 3, [4], 5, [6, [7, [], 8, [9]]]]
flatten_list(list_a)
print(list_a)


