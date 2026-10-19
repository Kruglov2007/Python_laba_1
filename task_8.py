# Программа случайно загадывает число от 1 до 100.
#  Пользователь вводит догадки.
#  Программа подсказывает «Больше» или «Меньше».
#  Игра продолжается, пока пользователь не угадает

import random
num=random.randint(1, 100)

while True:
    user_ans=int(input("Ваше число: "))
    if user_ans<num:
        print("Больше")
    elif user_ans>num:
        print("Меньше")
    else:
        print("Угадал!")
        break