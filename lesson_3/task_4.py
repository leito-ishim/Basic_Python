def my_func_1(x=1, y=-1):

    """Реализация через оператор **"""

    while True:
        try:
            x = float(input("Введите действительное положительное число: "))
            if x <= 0:
                raise Exception
            break
        except ValueError:
            print("Необходимо ввести число")
        except Exception:
            print("Необходимо ввести положительное число")
    while True:
        try:
            y = int(input("Введите целое отрицательное число: "))
            if y >= 0:
                raise Exception
            break
        except ValueError:
            print("Необходимо ввести число")
        except Exception:
            print("Необходимо ввести отрицательное число")
    return x ** y


def my_func_2(x, y):

    """Реализация через цикл"""

    total = 1
    for _ in range(0, int(y), -1):
        total *= (1 / float(x))
    return total


print(my_func_2(5, -5))

print(my_func_1())


