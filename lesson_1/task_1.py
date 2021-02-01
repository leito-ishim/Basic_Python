name = input("Введите Ваше имя: ")
sur_name = input("Введите Вашу фамилию: ")

# Проверка на ввод числа
while True:
    birthday = input("Введите год рождения: ")
    if birthday.isdigit():
        birthday = int(birthday)
        break
    print("Необходимо ввести число")
print(f"Приветствую тебя, {name} {sur_name}. Ты родился в {birthday} году, "
      f"значит в этом году тебе исполнится, или уже исполнилось {2021 - birthday} год(а)/лет")

