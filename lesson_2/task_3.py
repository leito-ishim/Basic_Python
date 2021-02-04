month_dict = {1: "январь", 2: 'февраль', 3: 'март', 4: 'апрель', 5: 'май', 6: 'июнь', 7: 'июль', 8: 'август', 9: 'сентябрь',
         10: 'октябрь', 11: 'ноябрь', 12: 'декабрь'}

season_dict = {1: "зима", 2: 'зима', 3: 'весна', 4: 'весна', 5: 'весна', 6: 'лето', 7: 'лето', 8: 'лето', 9: 'осень',
         10: 'осень', 11: 'осень', 12: 'зима'}

month_list = []

while True:
    number = input("Введите номер месяц:  ")
    if not number.isdigit():
        print("Необходимо ввести целое положительное число")
    elif int(number) > 12 or int(number) == 0:
        print("Необходимо ввести число от 1 до 12")
    else:
        break

for i in range(1, 13):
    month_list.append(month_dict.get(i))

print(f"Число {number} соответствует месяцу\nВ словаре: {month_dict.get(int(number))}, время года: "
      f"{season_dict.get(int(number))}\nВ списке: {month_list[int(number) - 1]}")






