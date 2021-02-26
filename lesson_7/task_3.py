class Cell:

    def __init__(self, num_cell):
        self.num_cell = int(num_cell)

    def __add__(self, other):
        return self.num_cell + other.num_cell

    def __sub__(self, other):
        return self.num_cell - other.num_cell if self.num_cell - other.num_cell > 0 else "Разница меньше или равна 0!"

    def __mul__(self, other):
        return self.num_cell * other.num_cell

    def __truediv__(self, other):
        return self.num_cell // other.num_cell

    def make_order(self, num):
        return ("*" * num + "\n") * (self.num_cell // int(num)) + "*" * (self.num_cell % int(num))


a = Cell(135)
b = Cell(6)

print(a + b)
print(a - b)
print(a * b)
print(a / b)

print(a.make_order(12))
