# Пользователь вводит список чисел. Числа вводятся через пробел, могут быть
# как целые, так и с плавающей точкой. Выведите на экран:
# 1. Уникальные числа.
# 2. Повторяющиеся числа.
# 3. Четные и нечетные чисел.
# 4. Отрицательные чисел.
# 5. Числа с плавающей точкой.
# 6. Сумму всех чисел, кратных 5.
# 7. Самое большое число.
# 8. Самое маленькое число.
try:
    num=[float(x) for x in input("Введите числа через пробел:").split()]
    def format_num(x):
        return int(x) if x.is_integer() else x
    print("Уникальные числа:", set(num))
    repeat=[format_num(x) for x in num if num.count(x)>1]
    print(f"Повторяющиеся числа:{set(repeat)}")
    ch=[format_num(x) for x in num if x.is_integer() and x%2==0]
    nch=[format_num(x) for x in num if x.is_integer() and x%2!=0]
    print(f"Чётные:{set(ch)}\nНечётные:{set(nch)}")
    negativ=[format_num(x) for x in num if x<0]
    print(f"Отрицательные числа:{negativ}")
    fl_num=[x for x in num if x-int(x)!=0]
    print(f"Числа с плавающей точкой:{fl_num}")
    five_cr=[x for x in num if x%5==0]
    total_sum=0
    for number in five_cr:
        total_sum+=number
    print(f"Сумма чисел кратных пяти:{total_sum}")
    print(f"Максимальное:{max(num)}")
    print(f"Минимальное:{min(num)}")
except:
    print("Вы неправильно ввели числа!")
