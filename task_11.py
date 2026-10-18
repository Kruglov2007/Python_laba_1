# Создайте экспертную систему для оценки кредитного риска.
# Входные параметры:
#  возраст заемщика;
#  ежемесячный доход;
#  размер запрашиваемого кредита;
#  срок кредита (месяцы);
#  кредитная история (отличная/хорошая/удовлетворительная/плохая);
#  наличие поручителей;
#  наличие залога.
# Система должна:
#  рассчитать соотношение кредита к доходу;
#  определить категорию риска (низкий/средний/высокий/критический);
#  предложить процентную ставку;
#  дать рекомендации по одобрению/отклонению

try:
    age = int(input("Возраст: "))
    pay = float(input("Доход: "))
    credit = float(input("Сумма кредита: "))
    time = int(input("Срок(месяцы): "))
    
    print("Кредитная история (отличная, хорошая, удовлетворительная, плохая):")
    history = input().strip().lower()
    
    is_helper = input("Есть поручители? (да/нет): ").strip().lower() == "да"
    is_money = input("Есть залог? (да/нет): ").strip().lower() == "да"

    coef_dohoda = credit / pay

    if history == "плохая" or age < 18 or (age > 70 and not is_money):
        risk_category = "Критический"
        interest_rate = "Не применяется"
        recommendation = "ОТКЛОНЕНО. Слишком высокие риски."

    
    elif (history == "удовлетворительная" or coef_dohoda > 10) and not is_money and not is_helper:
        risk_category = "Высокий"
        interest_rate = "22%"
        recommendation = "ОДОБРЕНО С УСЛОВИЯМИ (высокий риск, требуется поручитель или залог)."

    
    elif history == "отличная" and coef_dohoda <= 10:
        risk_category = "Низкий"
        interest_rate = "12%"
        recommendation = "ОДОБРЕНО. Максимально выгодные условия."

    
    elif history == "хорошая" or history == "отличная" or history == "удовлетворительная" or coef_dohoda > 10:
        risk_category = "Средний"
        interest_rate = "15%" if history in ["хорошая", "отличная"] else "18%"
        recommendation = "ОДОБРЕНО под обеспечение или на стандартных условиях."
        
    else:
        risk_category = "Неизвестно"
        interest_rate = "20%"
        recommendation = "ТРЕБУЕТСЯ ДОПОЛНИТЕЛЬНАЯ ПРОВЕРКА."

    
    print("\n--- РЕЗУЛЬТАТЫ ---")
    print(f"Соотношение кредит/доход: {coef_dohoda:.2f}")
    print(f"Категория риска: {risk_category}")
    print(f"Предложенная ставка: {interest_rate}")
    print(f"Решение: {recommendation}")
    
except ValueError:
    print("Введено неверное значение!")
