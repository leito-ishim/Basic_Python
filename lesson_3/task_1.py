def division():

    """Функция запрашивает у пользователя 2 числа и возвращает результат деления первого на второе число"""

    while True:
        try:
            num_1 = float(input("Введите первое число: "))
            break
        except ValueError:
            print("Необходимо ввести число")
    while True:
        try:
            num_2 = float(input("Введите второе число: "))
            if num_2 == 0:
                raise Exception
            break
        except ValueError:
            print("Необходимо ввести число")
        except Exception:
            print("На ноль делить нельзя")
    return num_1 / num_2


print(division())
