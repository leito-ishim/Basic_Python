class Worker:

    _income = {
        "wage": int(),
        "bonus": int()
    }

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {
            "wage": int(wage),
            "bonus": int(bonus)
        }

class Position(Worker):

    def get_full_name(self):
        print(f"Имя сотрудника {self.name} {self.surname}, его должность {self.position}")

    def get_total_income(self):
        print(f"Доход сотрудника {self.name} {self.surname} с учетом премии"
              f" составоляет {self._income.get('wage') + self._income.get('bonus')}")


a = Position("Nikita", "Kozlov", "Engineer", 23000, 12000)


a.get_full_name()
a.get_total_income()


