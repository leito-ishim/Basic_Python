class ComplexNum:

    def __init__(self, a, b):
        self.complex_num = complex(a, b)

    def __add__(self, other):
        return self.complex_num + other.complex_num

    def __mul__(self, other):
        return self.complex_num * other.complex_num


num1 = (15, 9)
num2 = (7, 0)

a = ComplexNum(num1[0], num1[1])
b = ComplexNum(num2[0], num2[1])

print(a + b)
print(a * b)

print(f"Проверка сложения: {num1[0] + num2[0]} + {num1[1] + num2[1]}j")
print(f"Проверка умножения: {num1[0] * num2[0] - (num1[1] * num2[1])} + {num1[0] * num2[1] + num1[1] * num2[0]}j")
