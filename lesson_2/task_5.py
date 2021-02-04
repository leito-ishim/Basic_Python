my_list = [7, 5, 3, 3, 2]

print(f"Рейтинг: {my_list}")

while True:
    n = input("Введите элемент рейтинга. Для выхода из программы введите не целое положительное число: ")
    if not n.isdigit():
        break
    else:
        n = int(n)
        for i in range(0, len(my_list)):
            if n > my_list[i]:
                my_list.insert(i, n)
                break
            if i == len(my_list) - 1:
                my_list.append(n)
    print(f"Новый рейтинг {my_list}")


