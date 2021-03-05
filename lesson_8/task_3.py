my_list = []

while True:
    num = input("Введите число. Для выхода из программы введите Stop: ")
    try:
        if num.lower() == "stop":
            break
        num = float(num)

    except ValueError:
        print("Необходимо ввести число!")
    else:
        my_list.append(num)
    finally:
        print(my_list)

