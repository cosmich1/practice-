print("Расчет стоимости разговора по двум тарифам")

# Ввод и проверка длительности разговора
minutes_str = input("Введите длительность разговора в минутах: ")
if not minutes_str.replace('.', '', 1).isdigit():
    print("Ошибка: Введено некорректное или отрицательное число минут.")
else:
    minutes = float(minutes_str)

    # Ввод и проверка дня недели
    day_str = input("Введите день недели (1 - Понедельник, ..., 7 - Воскресенье): ")
    if not day_str.isdigit():
        print("Ошибка: День недели должен быть целым числом.")
    else:
        day_of_week = int(day_str)
        
        if day_of_week < 1 or day_of_week > 7:
            print("Ошибка: День недели должен быть числом от 1 до 7.")
        else:
            # Параметры тарифов
            rate_A = 5.0  # руб/мин
            
            conn_fee_B = 20.0  # руб за соединение
            rate_B = 3.0  # руб/мин

            # Расчет базовой стоимости
            cost_A = minutes * rate_A
            
            # Если 0 минут, то и за соединение не платим
            if minutes > 0:
                cost_B = conn_fee_B + (minutes * rate_B)
            else:
                cost_B = 0.0

            # Проверка условий для скидки в выходные
            if day_of_week == 6 or day_of_week == 7:
                discount = 0.20  # 20% скидка
                cost_A = cost_A * (1 - discount)
                cost_B = cost_B * (1 - discount)
                print("\n Применена скидка 20% (выходной день)!")
            else:
                print("\nСкидка не применена (будний день).")

            # Вывод результатов и сравнение тарифов
            print(f"Стоимость по Тарифу А: {cost_A:.2f} руб.")
            print(f"Стоимость по Тарифу Б: {cost_B:.2f} руб.")

            if cost_A < cost_B:
                print(" Выгоднее использовать Тариф А.")
            elif cost_B < cost_A:
                print(" Выгоднее использовать Тариф Б.")
            else:
                print(" Стоимость по обоим тарифам одинакова.")
