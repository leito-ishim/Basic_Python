def my_func():
    total = 0
    while True:
        num_str = input("Введите строку чисел, разделенных пробелом. Для выхода из программы наберите 'q': ")
        for i in num_str.split():
            if i == "q":
                return print(f"Сумма введеных чисел равна: {total}")
            total += float(i)
        print(f"Сумма введеных чисел равна: {total}")


my_func()
