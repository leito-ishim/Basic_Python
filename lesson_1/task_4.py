# Проверка на ввод числа
while True:
    number = input("Введите целое положительное число: ")
    if not number.isdigit():
        print("Необходимо ввести число")
        continue
    else:
        number = int(number)
        break

max_number = 0

while number > 0:
    if (number % 10) > max_number:
        max_number = number % 10
    number //= 10
    if max_number == 9:
        break
print(max_number)
