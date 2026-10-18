# Создайте универсальный конвертер различных единиц измерения (не менее
# 10). Программа должна запрашивать тип измерения, исходную единицу,
# целевую единицу и значение.

print(" Универсальный конвертер единиц ")

print("Выберите тип измерения:")
print("1 - Длина (м, км, см, мили)")
print("2 - Масса (кг, г, фунты)")
print("3 - Температура (C, F, K)")

measurement_type = input("Введите номер типа (1, 2 или 3): ")

try:
    # длина
    if measurement_type == "1":
        print("\nДоступные единицы: м, км, см, мили")
        source = input("Исходная единица: ")
        target = input("Целевая единица: ")
        value = float(input("Введите значение (число): ")) # Тут может быть ошибка ввода!
        
        if source == "м": meters = value
        elif source == "км": meters = value * 1000
        elif source == "см": meters = value / 100
        elif source == "мили": meters = value * 1609.34
        else: meters = -1
        if meters == -1:
            print("Ошибка: неверная исходная единица.")
        else:
            if target == "м": result = meters
            elif target == "км": result = meters / 1000
            elif target == "см": result = meters * 100
            elif target == "мили": result = meters / 1609.34
            else: result = -1

            if result == -1:
                print("Ошибка: неверная целевая единица.")
            else:
                print(f"Результат: {value} {source} = {round(result, 4)} {target}")

    # масса
    elif measurement_type == "2":
        print("\nДоступные единицы: кг, г, фунты")
        source = input("Исходная единица: ")
        target = input("Целевая единица: ")
        value = float(input("Введите значение (число): ")) # Тут может быть ошибка ввода!
        
        if source == "кг": kg = value
        elif source == "г": kg = value / 1000
        elif source == "франты" or source == "фунты": kg = value * 0.453592
        else: kg = -1

        if kg == -1:
            print("Ошибка: неверная исходная единица.")
        else:
            if target == "кг": result = kg
            elif target == "г": result = kg * 1000
            elif target == "фунты": result = kg / 0.453592
            else: result = -1

            if result == -1:
                print("Ошибка: неверная целевая единица.")
            else:
                print(f"Результат: {value} {source} = {round(result, 4)} {target}")

    # температура
    elif measurement_type == "3":
        print("\nДоступные единицы: C, F, K")
        source = input("Исходная единица: ")
        target = input("Целевая единица: ")
        value = float(input("Введите значение (число): ")) # Тут может быть ошибка ввода!
        
        # Переводим в Цельсий
        if source.upper() == "C" or source == "С": celsius = value
        elif source.upper() == "F": celsius = (value - 32) * 5 / 9
        elif source.upper() == "K": celsius = value - 273.15
        else: celsius = -999

        if celsius == -999:
            print("Ошибка: неверная исходная единица.")
        else:
            if target.upper() == "C" or target == "С": result = celsius
            elif target.upper() == "F": result = (celsius * 9 / 5) + 32
            elif target.upper() == "K": result = celsius + 273.15
            else: result = -999

            if result == -999:
                print("Ошибка: неверная целевая единица.")
            else:
                print(f"Результат: {value} {source} = {round(result, 2)} {target}")

    else:
        print("Ошибка: выбран неверный тип измерения.")


except ValueError:
    print("Ошибка: Вы ввели текст вместо числа! Пожалуйста, используйте цифры.")
