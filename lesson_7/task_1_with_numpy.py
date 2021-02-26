import numpy as np


class Matrix:

    def __init__(self, my_matrix):
        self.my_matrix = my_matrix

    def __add__(self, other):
        return Matrix(np.array(self.my_matrix + np.array(other.my_matrix)))

    def __str__(self):
        my_str = ""
        for i in self.my_matrix:
            for j in i:
                my_str += str(j) + "\t"
            my_str += "\n"
        return my_str[:-1]


a = Matrix([
    [11, 22, 3],
    [4, 55, 6],
    [7, 8, 0]
])

b = Matrix([
    [3, 5, 3],
    [1, 44, 4],
    [6, 34, 6]
])

print(a + b)
