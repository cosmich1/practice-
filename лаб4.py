## объявляем пустой массив и заполняем его 10 числами с клавиатуры
arr = []
for i in range(10):
    num = float(input(f"Введите элемент [{i}]: "))
    arr.append(num)

## выводим исходный массив в одну строку
print("Массив:", end=" ")
for x in arr:
    print(x, end=" ")
print()

## инициализируем переменные для расчётов первым элементом массива
total_sum = 0
min_val = arr[0]
max_val = arr[0]
min_idx = 0
max_idx = 0

## проходим по индексам массива для поиска суммы, min и max
for i in range(len(arr)):
    total_sum += arr[i]  # накапливаем сумму элементов

    if arr[i] < min_val:
        min_val = arr[i]
        min_idx = i  # запоминаем индекс нового минимума

    if arr[i] > max_val:
        max_val = arr[i]
        max_idx = i  # запоминаем индекс нового максимума

## вычисляем среднее арифметическое
avg_val = total_sum / len(arr)

## выводим результаты
print(f"Сумма элементов: {total_sum}")
print(f"Среднее арифметическое: {avg_val}")
print(f"Минимум: {min_val} (индекс {min_idx})")
print(f"Максимум: {max_val} (индекс {max_idx})")
