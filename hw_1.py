class Matrix:

    def __init__(self, list_of_lists):

        self.matrix = []

        for i in range(len(list_of_lists)):
            self.matrix.append([*map(float, list_of_lists[i])])

    def __str__(self):
        return str(self.matrix)

    def __add__(self, other):
        other_matrix = other.matrix
        result = []
        flow = []
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                _sum = self.matrix[i][j] + other_matrix[i][j]
                flow.append(_sum)
                if len(flow) == len(self.matrix[i]):
                    result.append(flow)
                    flow = []

        return Matrix(result)


# test
my_matrix1 = Matrix([[1, 2, 3, 4], [4, 3, 2, 1]])
my_matrix2 = Matrix([[5, 6, 7, 8], [8, 7, 6, 5]])

print(f"{str(my_matrix1)} + {str(my_matrix1)} = \n {my_matrix1 + my_matrix2}")