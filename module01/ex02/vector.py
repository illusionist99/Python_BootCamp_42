import decimal


def float_range(start, stop, step):
    while start < stop:
        yield float(start)
        start += float(decimal.Decimal(step))


class Vector:

    def __init__(self, *args):
        if type(args[0]) is list and len(args) == 1:
            self.values = args[0]
            self.size = len(self.values)
        elif str(args[0]).isdigit() and len(args) == 1:
            self.values = list(float_range(1.0, int(args[0]), 1.0))
            self.size = len(self.values)
        elif str(args[0]).isdigit() and str(args[1]).isdigit() and len(args) == 2:
            self.values = list(float_range(int(args[0]), int(args[1]), 1.0))
            self.size = len(self.values)

    def __str__(self):
        return "{}".format(self.values)

    def __add__(self, other):
        index = 0
        ret = []
        if isinstance(other, Vector):
            if other.size == self.size:
                while index < self.size:
                    ret.append(other.values[index] + self.values[index])
                    index += 1
            else:
                raise ValueError
        else:
            while index < self.size:
                ret.append(other + self.values[index])
                index += 1
        return ret

    __radd__ = __add__

    def __rsub__(self, other):
        index = 0
        ret = []
        if isinstance(other, Vector):
            if other.size == self.size:
                while index < self.size:
                    ret.append(other.values[index] - self.values[index])
                    index += 1
            else:
                raise ValueError
        else:
            while index < int(self.size):
                ret.append(self.values[index] - other)
                index += 1
        return ret

    def __sub__(self, other):
        index = 0
        ret = []
        if isinstance(other, Vector):
            if other.size == self.size:
                while index < self.size:
                    ret.append(self.values[index] - other.values[index])
                    index += 1
            else:
                raise ValueError
        else:
            while index < int(self.size):
                ret.append(- self.values[index] + other)
                index += 1
        return ret

    def __truediv__(self, other):
        index = 0
        ret = []
        if isinstance(other, Vector):
            if other.size == self.size:
                while index < self.size:
                    try:
                        ret.append(self.values[index] / other.values[index])
                    except ZeroDivisionError:
                        print("Operation Not Allowed div By Zero")
                        exit(-1)
                    index += 1
            else:
                raise ValueError
        else:
            while index < int(self.size):
                try:
                    ret.append(self.values[index] / other)
                except ZeroDivisionError:
                    print("Operation Not Allowed div By Zero")
                    exit(-1)
                index += 1
        return ret

    def __rtruediv__(self, other):
        index = 0
        ret = []
        if isinstance(other, Vector):
            if other.size == self.size:
                while index < self.size:
                    try:
                        ret.append(other.values[index] / self.values[index])
                    except ZeroDivisionError:
                        print("Operation Not Allowed div By Zero")
                        exit(-1)
                    index += 1
            else:
                raise ValueError
        else:
            while index < int(self.size):
                try:
                    ret.append(other / self.values[index])
                except ZeroDivisionError:
                    print("Operation Not Allowed div By Zero")
                    exit(-1)
                index += 1
        return ret

    def __mul__(self, other):
        index = 0
        ret = []
        if isinstance(other, Vector):
            if other.size == self.size:
                while index < self.size:
                    ret.append(other.values[index] * self.values[index])
                    index += 1
            else:
                raise ValueError
        else:
            while index < int(self.size):
                ret.append(self.values[index] * other)
                index += 1
        return ret

    __rmul__ = __mul__

    def __repr__(self):
        return '{} sized Vector with values : \n{}'.format(self.size, ", ".join(map(str, self.values)))
