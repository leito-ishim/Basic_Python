while True:
    proceeds = input("Введите выручку предприятия, руб: ")
    try:
        temp_proceeds = float(proceeds)
    except ValueError:
        print("Необходимо ввести число")
    else:
        proceeds = float(proceeds)
        break
while True:
    costs = input("Введите издержки предприятия, руб: ")
    try:
        temp_costs = float(costs)
    except ValueError:
        print("Необходимо ввести число")
    else:
        costs = float(costs)
        break
if proceeds < costs:
    print("Предприятие работает в убыток")
elif proceeds == costs:
    print('Предприятие работает в "ноль"')
else:
    print(f"Предприятие работает с прибылью! Рентабельность предприятия составяет: {(proceeds - costs) / proceeds * 100} %")
    while True:
        number_employee = input("Введите количество сотрудников: ")
        if not number_employee.isdigit():
            print("Необходимо ввести целое положительное число")
            continue
        else:
            number_employee = int(number_employee)
            break
    print(f"Прибыль предприятия в расчете на одного сотрудника составляет: {(proceeds - costs) / number_employee:.2f} руб")


