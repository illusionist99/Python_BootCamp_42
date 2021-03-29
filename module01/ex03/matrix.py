

def shape(lst):
    rows = len(lst)
    cols = len(lst[0])
    t = (rows, cols)
    return t


class Matrix:
    def __init__(self, matrix):
        lst = []
        count = 0
        if isinstance(matrix, tuple) and len(matrix) == 2:
            for i in range(matrix[0]):
                lst_small = []
                for j in range(matrix[1]):
                    lst_small.append(float(count))
                    count += 1

                lst.append(lst_small)
            self.shape = matrix
            self.data = lst
        else:
            for vector in matrix:
                if not isinstance(vector, list):
                    exit("Received Type error")
            self.data = matrix
            self.shape = shape(matrix)
            for i in matrix:
                if not (isinstance(i, list) and len(i) == self.shape[1]):
                    exit("Received Type error")

    def is_valid(self):
        if isinstance(self, Matrix):
            for vector in self.data:
                if not isinstance(vector, list):
                    exit("Received Type error")
            for i in self.data:
                if not (isinstance(i, list) and len(i) == self.shape[1]):
                    exit("Received Type error")
            return True
        return False

    def __str__(self):
        return "(Matrix : {} Shape : {})".format(self.data, self.shape)

    def __add__(self, other):
        if Matrix.is_valid(self) and Matrix.is_valid(other) and self.shape == other.shape:
            lst = []
            for i in range(self.shape[0]):
                lst_small = []
                for j in range(self.shape[1]):
                    lst_small.append(float(self.data[i][j] + other.data[i][j]))
                lst.append(lst_small)
            return Matrix(lst)
        elif isinstance(other, int) or isinstance(other, float):
            lst = []
            for i in range(self.shape[0]):
                lst_small = []
                for j in range(self.shape[1]):
                    lst_small.append(float(self.data[i][j] + other))
                lst.append(lst_small)
            return Matrix(lst)
        else:
            exit("Received Type error")

    __radd__ = __add__

    def __sub__(self, other):
        if Matrix.is_valid(self) and Matrix.is_valid(other) and self.shape == other.shape:
            lst = []
            for i in range(self.shape[0]):
                lst_small = []
                for j in range(self.shape[1]):
                    lst_small.append(float(self.data[i][j] - other.data[i][j]))
                lst.append(lst_small)
            return Matrix(lst)
        elif isinstance(other, int) or isinstance(other, float):
            lst = []
            for i in range(self.shape[0]):
                lst_small = []
                for j in range(self.shape[1]):
                    lst_small.append(float(self.data[i][j] - other))
                lst.append(lst_small)
            return Matrix(lst)
        else:
            exit("Received Type error")

    def __rsub__(self, other):
        if Matrix.is_valid(self) and Matrix.is_valid(other) and self.shape == other.shape:
            lst = []
            for i in range(self.shape[0]):
                lst_small = []
                for j in range(self.shape[1]):
                    lst_small.append(float(- self.data[i][j] + other.data[i][j]))
                lst.append(lst_small)
            return Matrix(lst)
        elif isinstance(other, int) or isinstance(other, float):
            lst = []
            for i in range(self.shape[0]):
                lst_small = []
                for j in range(self.shape[1]):
                    lst_small.append(float(- self.data[i][j] + other))
                lst.append(lst_small)
            return Matrix(lst)
        else:
            exit("Received Type error")

    def __truediv__(self, other):
        if Matrix.is_valid(self) and Matrix.is_valid(other) and self.shape == other.shape:
            lst = []
            for i in range(self.shape[0]):
                lst_small = []
                for j in range(self.shape[1]):
                    try:
                        lst_small.append(float(self.data[i][j] / other.data[i][j]))
                    except ZeroDivisionError:
                        exit("Division by zero is no allowed")
                lst.append(lst_small)
            return Matrix(lst)
        elif isinstance(other, int) or isinstance(other, float):
            lst = []
            for i in range(self.shape[0]):
                lst_small = []
                for j in range(self.shape[1]):
                    try:
                        lst_small.append(float(self.data[i][j] / other))
                    except ZeroDivisionError:
                        exit("Division by zero is no allowed")
                lst.append(lst_small)
            return Matrix(lst)
        else:
            exit("Received Type error")

    def __rtruediv__(self, other):
        if Matrix.is_valid(self) and Matrix.is_valid(other) and self.shape == other.shape:
            lst = []
            for i in range(self.shape[0]):
                lst_small = []
                for j in range(self.shape[1]):
                    try:
                        lst_small.append(float(other.data[i][j] / self.data[i][j]))
                    except ZeroDivisionError:
                        exit("Division by zero is no allowed")
                lst.append(lst_small)
            return Matrix(lst)
        elif isinstance(other, int) or isinstance(other, float):
            lst = []
            for i in range(self.shape[0]):
                lst_small = []
                for j in range(self.shape[1]):
                    try:
                        lst_small.append(float(other / self.data[i][j]))
                    except ZeroDivisionError:
                        exit("Division by zero is no allowed")
                lst.append(lst_small)
            return Matrix(lst)
        else:
            exit("Received Type error")

    def __mul__(self, other):
        if Matrix.is_valid(self) and Matrix.is_valid(other) and self.shape == other.shape:
            lst = []
            count = 0
            print("Debug :")
            for i in range(self.shape[0]):
                lst_small = []
                for j in range(self.shape[1]):
                    print("Operation: ", end="")
                    for k in range(self.shape[0]):
                        print("{}".format(str(self.data[i][k]) + " * " + str(other.data[k][j])), end="")
                        count += float(self.data[i][k] * other.data[k][j])
                        if k % 2 == 0:
                            print("+ ", end="")
                    lst_small.append(count)
                    count = 0
                    print()
                lst.append(lst_small)
            return Matrix(lst)
        elif isinstance(other, int) or isinstance(other, float):
            lst = []
            for i in range(self.shape[0]):
                lst_small = []
                for j in range(self.shape[1]):
                    lst_small.append(float(other * self.data[i][j]))
                lst.append(lst_small)
            return Matrix(lst)
        else:
            exit("Received Type error")

    __rmul__ = __mul__
