# Проверка на ввод числа
while True:
    number_seconds = input("Введите количество секунд: ")
    if number_seconds.isdigit():
        number_seconds = int(number_seconds)
        break
    print("Необходимо ввести число")

print(f"{number_seconds // 3600:0{2}}:{(number_seconds % 3600) // 60:0{2}}:{(number_seconds % 3600) % 60:0{2}}")

