# Посчитайте общую сумму выручки по каждому товару (входные данные –
# список словарей, содержащих информацию о наименовании товара, его цене,
# количестве проданных единиц), выведите наименование самого прибыльного
# товара и найдите количество уникальных наименований.
sales_data = []

print("Введите информацию о товарах (для выхода введите пустую строку вместо названия).")

while True:
    
    name = input("\nВведите наименование товара: ").strip()
    
    # Если пользователь ничего не ввел, прерываем цикл ввода
    if not name:
        break
        
    try:
        price = float(input(f"Введите цену для '{name}': "))
        quantity = int(input(f"Введите количество проданных единиц: "))
    except ValueError:
        print("Ошибка: Цена и количество должны быть числами! Попробуйте ввести этот товар заново.")
        continue

    product = {
        "name": name,
        "price": price,
        "quantity": quantity
    }
    
    sales_data.append(product)
balance=0
max_cash=0
names={prod.get("name", '') for prod in sales_data}
best_product=''
for el in sales_data:
    balance+=el.get("price", 0)*el.get("quantity", 0)
    if el.get("price", 0)*el.get("quantity", 0)>max_cash:
        max_cash=el.get("price", 0)*el.get("quantity", 0)
        best_product=el.get("name", 'Не указан')
print(f"Выручка составила:{balance}")
print(f"Самый прибыльный товар-{best_product}")
print(f"Количество уникальных имён:{len(names)}")
