from sys import argv

script_name, name, working_out, rate, prize = argv

try:
    working_out = float(working_out)
    rate = float(rate)
    prize = float(prize)
    print(f"Зароботная плата сотрудника: {name} составляет: {int(working_out) * int(rate) + int(prize)} рублей.")
except ValueError:
    print("Последние три параметра должны быть числами")


