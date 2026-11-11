## функции расчёта площадей
def circle_area(r):
    "Считает площадь круга по радиусу."
    return 3.14 * r ** 2


def triangle_area(a, h):
    "Считает площадь треугольника по основанию и высоте."
    return 0.5 * a * h


def rect_area(a, b):
    "Считает площадь прямоугольника по двум сторонам."
    return a * b


## функция для проверки ввода
def get_positive_float(prompt):
    "Ввод положительного числа."
    val = 0
    while val <= 0:
        val = float(input(prompt))
    return val


## функция вывода
def print_result(name, area):
    "Вывод результата."
    print(f"Площадь {name}: {area:.2f}")


## основное меню программы
def main():
    "Основное меню программы."
    while True:
        print("\n1 - Круг")
        print("2 - Треугольник")
        print("3 - Прямоугольник")
        print("0 - Выход")

        choice = input("Выбор: ")

        ## обработка выбора пользователя
        if choice == "0":
            break
        elif choice == "1":
            r = get_positive_float("Радиус: ")
            print_result("круга", circle_area(r))
        elif choice == "2":
            a = get_positive_float("Основание: ")
            h = get_positive_float("Высота: ")
            print_result("треугольника", triangle_area(a, h))
        elif choice == "3":
            a = get_positive_float("Ширина: ")
            b = get_positive_float("Длина: ")
            print_result("прямоугольника", rect_area(a, b))
        else:
            print("Неверный пункт меню")


main()