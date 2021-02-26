
class Matrix:

    def __init__(self, my_matrix):
        self.my_matrix = my_matrix

    def __add__(self, other):
        my_matrix = [[]]
        for i in range(0, len(self.my_matrix)):
            my_list= []
            for j in range(0, len(self.my_matrix[i])):
                my_list.insert(j, self.my_matrix[i][j] + other.my_matrix[i][j])
            my_matrix.insert(i, my_list)
        return Matrix(my_matrix)

    def __str__(self):
        my_str = ""
        for i in self.my_matrix:
            for j in i:
                my_str += str(j) + "\t"
            my_str += "\n"
        return my_str


a = Matrix([
    [11, 22, 3],
    [4, 55, 6],
    [7, 8, 9]
])

b = Matrix([
    [3, 5, 3],
    [1, 44, 4],
    [6, 34, 6]
])
print(a)
print(a + b)
