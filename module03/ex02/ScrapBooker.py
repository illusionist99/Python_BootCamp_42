import numpy

class ScrapBooker:

    @staticmethod
    def crop(array, dimensions, position=(0, 0)):
        """
        crops the image as a rectangle with the given dimensions
        (meaning, the new height and width for the image)
        whose top left corner is given by the position argument.
        The position should be (0,0) by default. You have to consider it an error (and handle said error)
        if dimensions is larger than the current image size.
        :param array: NumPy Array
        :param dimensions:
        :param position:
        :return: NumPy Array
        """
        new_array = array[position[0]:dimensions[0], position[1]:dimensions[1]]

        return new_array

    @staticmethod
    def thin(array, n, axis):
        """
        deletes every n-th pixel row along the specified axis (0 vertical, 1 horizontal), example below.
        :param array:
        :param n:
        :param axis:
        :return:
        """
        new_array = []
        if axis == 0:
            for i in range(len(array)):
                lst = []
                for j in range(len(array[i])):
                    if not (j + 1) % n == 0:
                        lst.append(array[i][j])
                new_array.append(lst)
        elif axis == 1:
            for i in range(len(array)):
                if not (i + 1) % n == 0:
                    new_array.append(array[i])
        return numpy.asarray(new_array)

    @staticmethod
    def juxtapose(array, n, axis):
        """
        juxtaposes n copies of the image along the specified axis (0 vertical, 1 horizontal).
        :param array:
        :param n:
        :param axis:
        :return:
        """
        c = array
        for i in range(n):
            c = numpy.concatenate((c, array), axis, dtype=type(array))
        return c

    @staticmethod
    def mosaic(array, dimensions):
        """
        makes a grid with multiple copies of the array.
        The dimensions argument specifies the dimensions
        (meaning the height and width) of the grid (e.g. 2x3).
        :param array:
        :param dimensions:
        :return:
        """
        y = dimensions[0]
        x = dimensions[1]
        big_lst = []
        sub_list = []

        print(x, y)
        if y > 0:
            for j in range(len(array) + y):
             sub_list = []
             if x > 0:
                j = j % len(array)
                for i in range(len(array[j]) + x):
                    i = i % len(array[j])
                    sub_list.append(array[j][i][:x])
                big_lst.append(sub_list)
        return numpy.asarray(big_lst)

array = numpy.chararray((11, 12), unicode=True)
i = 0
j = 0
while j < 11:
    while i < 12:
        array[j][i] = chr(65 + i)
        i += 1
    i = 0
    j += 1

new_array = ScrapBooker.thin(array, n=4, axis=1)
n = ScrapBooker.juxtapose(array, 1, 1)
print(new_array)
m = ScrapBooker.mosaic(array, (2, 2))
print(m)
#print(n)

