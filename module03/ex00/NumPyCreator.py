import numpy as np
import random
class NumPyCreator:

    @staticmethod
    def from_list(lst, dtype=None):
        """
        Takes in a List and returns its corresponding Numpy array
        """
        if isinstance(lst, list):
            if dtype is None:
                return np.array(lst)
            else:
                return np.array(lst, dtype)
        else:
            exit("first Param Must Be a List")

    @staticmethod
    def from_tuple(tpl, dtype=None):
        """
        Takes in a Tuple and returns its corresponding Numpy array
        """
        if isinstance(tpl, tuple):
            if dtype is None:
                return np.array(tpl)
            else:
                return np.array(tpl, dtype)
        else:
            exit("first Param Must Be a Tuple")

    @staticmethod
    def from_iterable(itr, dtype=None):
        """
        Takes in an iterable and returns an array which contains all of it's elements
        """
        try:
            iter(itr)
        except TypeError:
            exit("Second Argument must be iterable")
        if dtype is None:
            return np.array(itr)
        else:
            return np.array(itr, dtype)

    @staticmethod
    def from_shape(shape, value=0):
        if len(shape) > 2:
            exit("Shape Must be of 2 dimensions (x, y)")
        y = int(shape[0])
        x = int(shape[1])
        rt = []

        for j in range(y):
            sml_lst = []
            for i in range(x + 1):
                sml_lst.append(value)
            rt.append(sml_lst)
        return rt

    @staticmethod
    def random(shape, dtype=None):
        if len(shape) > 2:
            exit("Shape Must be of 2 dimensions (x, y)")
        y = int(shape[0])
        x = int(shape[1])
        rt = []

        for j in range(y):
            sml_lst = []
            for i in range(x + 1):
                sml_lst.append(random.random())
            rt.append(sml_lst)
        return rt

    @staticmethod
    def identity(n, dtype=None):
        if not isinstance(n, int):
            exit("N must be an int")
        y = n
        x = n - 1
        rt = []
        for j in range(y):
            sml_lst = []
            for i in range(x + 1):
                if i == j:
                    sml_lst.append(1)
                else:
                    sml_lst.append(0)
            rt.append(sml_lst)
        return rt


lstt = [[1, 2, 3], [4, 5, 6.6]]
obj = NumPyCreator
NumPyCreator.from_list(lstt, float)
shp = (3, 6)
print(NumPyCreator.from_shape(shp))
print(NumPyCreator.identity(9))

