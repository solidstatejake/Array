from ArrayTools.arrayClass import Array2D


class Matrix:

    # Note that all matrices are initialized to 0.
    def __init__(self, nrow, ncol):
        assert nrow > 0 and ncol > 0, "Number of rows and columns must both be greater than 0."
        self.nrow = nrow
        self.ncol = ncol
        self.matrix = Array2D(nrow, ncol)

    def __getitem__(self, index_tuple):
        return self.matrix[index_tuple[0], index_tuple[1]]

    def __setitem__(self, index_tuple, value):
        self.matrix[index_tuple[0], index_tuple[1]] = value

    def __add__(self, matrix):
        assert self.nrow == matrix.nrow and self.ncol == matrix.ncol, "Matrices must be of equivalent dimensions."
        new_matrix = Matrix(self.nrow, self.ncol)
        for i in range(self.matrix.nrow()):
            for j in range(self.matrix.ncol()):
                new_matrix.matrix[i, j] = self.matrix[i,j] + matrix.matrix[i,j]
        return new_matrix

    def __sub__(self, matrix):
        assert self.nrow == matrix.nrow and self.ncol == matrix.ncol, "Matrices must be of equivalent dimensions."
        new_matrix = Matrix(self.nrow, self.ncol)
        for i in range(self.matrix.nrow()):
            for j in range(self.matrix.ncol()):
                new_matrix.matrix[i, j] = self.matrix[i, j] - matrix.matrix[i, j]
        return new_matrix

    # Matrix multiplication of mxn * nxp = mxp
    def __mul__(self, matrix):
        assert self.ncol == matrix.nrow,  "Matrices must be of proper dimensions for matrix multiplication."
        new_matrix = Matrix(self.nrow, matrix.ncol)
        sum = 0
        number = 1
        for i in range(self.nrow):
            for j in range(matrix.ncol):
                for count in range(self.ncol):
                    sum += self.matrix[i, count] * matrix.matrix[count, j]
                    print("The number of operations thus far is: " + str(number))
                    number += 1
                    if count == self.ncol - 1:
                        new_matrix[i, j] = sum
                        sum = 0
        return new_matrix

    def transpose(self):
        new_matrix = Matrix(self.nrow, self.ncol)
        for i in range(self.nrow):
            for j in range(self.ncol):
                new_matrix.matrix[i, j] = self.matrix[j, i]
        return new_matrix

    def print(self):
        for i in range(self.nrow):
            for j in range(self.ncol):
                print(self.matrix[i, j]) if j == self.ncol - 1 else print(self.matrix[i, j], end=' ')
