print("Давайте создадим список")
num = int(input("Из скольки элементов будет состоять список: "))

my_list = []

while num:
    my_list.append(input("Введите элемент списка: "))
    num -= 1
print(f"Ваш список:\t\t\t{my_list}")

for i in range(0, len(my_list) if len(my_list) % 2 == 0 else (len(my_list) - 1), 2):
    my_list[i], my_list[i+1] = my_list[i+1], my_list[i]

print(f"Измененный список:\t{my_list}")


