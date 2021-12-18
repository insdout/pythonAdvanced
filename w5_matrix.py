import copy


class MatrixSizeError(Exception):
    pass


class Matrix:
    # Part 1
    def __init__(self, matrix):
        self.matrix = copy.deepcopy(matrix)

    def __str__(self):
        line = ""
        for row in self.matrix:
            line += "\t".join(map(str, row)) + "\n"
        return line[:-1]

    # Part 2
    def __eq__(self, other):
        if not isinstance(other, Matrix):
            raise TypeError
        return self.matrix == other.matrix

    def size(self):
        len_rows = [len(row) for row in self.matrix]
        a = max(len_rows)
        if len(set(len_rows)) == 1:
            return tuple([len(self.matrix), max(a, 1)])

    # Part 3
    def __add__(self, other):
        result_matrix = []
        if not isinstance(other, Matrix):
            raise TypeError
        if self.size() != other.size():
            raise MatrixSizeError
        for row_1, row_2 in zip(self.matrix, other.matrix):
            result_matrix.append([a + b for a, b in zip(row_1, row_2)])
        return Matrix(result_matrix)

    def __sub__(self, other):
        result_matrix = []
        if not isinstance(other, Matrix):
            raise TypeError
        if self.size() != other.size():
            raise MatrixSizeError
        for row_1, row_2 in zip(self.matrix, other.matrix):
            result_matrix.append([a - b for a, b in zip(row_1, row_2)])
        return Matrix(result_matrix)

    # Part 4
    def __mul__(self, other):
        if not isinstance(other, Matrix):
            raise TypeError
        if self.size()[1] != other.size()[0]:
            raise MatrixSizeError
        zip_b = zip(*other.matrix)
        zip_b = list(zip_b)
        return Matrix([[sum(
            ele_a * ele_b for ele_a, ele_b in zip(row_a, col_b))
                 for col_b in zip_b] for row_a in self.matrix])

    # Part 5
    def transpose(self):
        zip_b = zip(*self.matrix)
        zip_b = list(map(list, zip_b))
        return Matrix(zip_b)

    # Part 6
    def tr(self):
        trace = 0
        if self.size()[0] != self.size()[1]:
            raise MatrixSizeError
        for i in range(self.size()[0]):
            trace += self.matrix[i][i]
        return trace

    def det(self):
        if self.size()[0] != self.size()[1]:
            raise MatrixSizeError

        def determinant(matrix, mul):

            width = len(matrix)
            if width == 1:
                return mul * matrix[0][0]
            else:
                sign = -1
                answer = 0
                for i in range(width):
                    m = []
                    for j in range(1, width):
                        buff = []
                        for k in range(width):
                            if k != i:
                                buff.append(matrix[j][k])
                        m.append(buff)
                    sign *= -1
                    answer = answer + mul * determinant(m, sign * matrix[0][i])
            return answer
        return determinant(self.matrix, 1)
