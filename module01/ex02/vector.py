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
        while index < int(self.size):
            ret.append(self.values[index] + other)
            index += 1
        return ret

    __radd__ = __add__

    def __sub__(self, other):
        index = 0
        ret = []
        while index < int(self.size):
            ret.append(self.values[index] - other)
            index += 1
        return ret

    def __rsub__(self, other):
        index = 0
        ret = []
        while index < int(self.size):
            ret.append(- self.values[index] + other)
            index += 1
        return ret
