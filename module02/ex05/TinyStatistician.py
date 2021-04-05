
" using for Loops !!!!"


def sqrt(n):
    if n < 0:
        return
    return n ** 0.5

class TinyStatistician:
    def mean(self, x):
        rt = 0
        if (not isinstance(x, list)) or x == []:
            return None
        for item in x:
            rt += float(item/len(x))
        return round(rt, 2)

    def median(self, x):
        if (not isinstance(x, list)) or x == []:
            return None
        index = 0
        x.sort()
        if len(x) % 2 != 0:
            index = int(len(x) / 2)
            rt = float(x[index])
        else:
            index = int(len(x) / 2)
            rt = float(x[index] + x[index - 1]) / 2
        return rt

    def quartiles(self, x, percentile):
        if (not isinstance(x, list)) or x == []:
            return None
        if not (percentile == 25 or percentile == 75):
            return None
        x.sort()
        index = int(len(x) * percentile / 100)
        return float(x[index])

    def var(self, x):
        mean = self.mean(x)
        if (not isinstance(x, list)) or x == []:
            return None
        result = 0
        for item in x:
            item = (item - mean) ** 2
            result += item
        return result/len(x)

    def std(self, x):
        varience = self.var(x)
        return sqrt(varience)


dataset = [-1, -2, -3, -4, 4, 3, 2, 1]
a = [1, 42, 300, 10, 59]
instance = TinyStatistician()
print()
print(instance.std(a))
