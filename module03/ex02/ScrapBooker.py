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
        return numpy.delete(array, n, axis)

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
            c = numpy.concatenate(c, array, axis)
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
        pass

