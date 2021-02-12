from math import factorial


def gen(n):
    temp = 1
    for el in range(1, int(n) + 1):
        temp *= el
        yield temp
        #yield factorial(el)


try:
    num = input("Введите факториал какого числа хотите получить: ")
    fact_list = [el for el in gen(num)]
    print(fact_list)
except ValueError:
    print("Необходимо ввести целое положительно число")