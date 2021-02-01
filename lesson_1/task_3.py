# Проверка на ввод числа
while True:
    number = input("Введите однозначное положительное число: ")
    if not number.isdigit():
        print("Необходимо ввести число")
        continue
    elif int(number) > 9 or int(number) < 1:
        print("Число должно быть однозначнным и положительным")
        continue
    else:
        number = int(number)
        break

print(f"n = {number}.\nn+nn+nnn = {number + (number * 10 + number) + (number * 100 + number * 10 + number)}")
