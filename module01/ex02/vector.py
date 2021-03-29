import decimal


def float_range(start, stop, step):
    while start < stop:
        yield float(start)
        start += float(decimal.Decimal(step))


def allowed(arg):
    if isinstance(arg, float) or isinstance(arg, int):
        return True
    return False


class Vector:

    def __init__(self, *args):
        if type(args[0]) is list and len(args) == 1:
            self.values = args[0]
            self.size = len(self.values)
        elif allowed(args[0]) and len(args) == 1:
            self.values = list(float_range(0, float(args[0]), 1.0))
            self.size = len(self.values)
        elif allowed(args[0]) and allowed(args[1]) and len(args) == 2:
            self.values = list(float_range(float(args[0]), float(args[1]), 1.0))
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
        return Vector(ret)

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
            while index < self.size:
                ret.append(- other + self.values[index])
                index += 1
        return Vector(ret)

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
        return Vector(ret)

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
            while index < self.size:
                try:
                    ret.append(self.values[index] / other)
                except ZeroDivisionError:
                    print("Operation Not Allowed div By Zero")
                    exit(-1)
                index += 1
        return Vector(ret)

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
        return Vector(ret)

    def __mul__(self, other):
        index = 0
        sum = 0
        ret = []
        if isinstance(other, Vector):
            if other.size == self.size:
                lst = zip(other.values, self.values)
                for x, y in lst:
                    sum += x * y
            else:
                raise ValueError
            return sum
        else:
            while index < int(self.size):
                ret.append(self.values[index] * other)
                index += 1
        return Vector(ret)

    __rmul__ = __mul__

    def __repr__(self):
        return '{} sized Vector with values : \n{}'.format(self.size, ", ".join(map(str, self.values)))

