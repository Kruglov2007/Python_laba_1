# Введите сумму в рублях (целое число). Определите, сколько купюр по 100, 50,
# 10, 5 и монет по 2 и 1 рублю потребуется для ее размена
cash = int(input("Введите сумму в рублях: "))

b100 = cash // 100
remainder = cash % 100
b50 = remainder // 50
remainder = remainder % 50
b10 = remainder // 10
remainder = remainder % 10
b5 = remainder // 5
remainder = remainder % 5
b2 = remainder // 2
b1 = remainder % 2

print(f"Для размена суммы {cash} руб. потребуется:")
print(f"Купюр по 100 руб.: {b100}")
print(f"Купюр по 50 руб.:  {b50}")
print(f"Купюр по 10 руб.:  {b10}")
print(f"Купюр по 5 руб.:   {b5}")
print(f"Монет по 2 руб.:   {b2}")
print(f"Монет по 1 руб.:   {b1}")
