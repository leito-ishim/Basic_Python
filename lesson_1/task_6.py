while True:
    number = input("Сколько спортсмен пробежал в первый день, км: ")
    if not number.isdigit():
        print("Необходимо ввести целое положительное число")
        continue
    else:
        number = int(number)
        break

while True:
    result = input("Какого результата необходимо достигнуть, км: ")
    if not result.isdigit():
        print("Необходимо ввести целое положительное число")
        continue
    else:
        result = int(result)
        break

num_days = 1

while number < result:
    print(f"{num_days}-й день: {number:.2f} км") # Строку можно убрать, оставлена для того чтобы видеть полные вычисления
    number *= 1.1
    num_days += 1

print(f"На {num_days}-й день спортсмен достигнет результата - {number:.2f} км (не менее {result} км).")