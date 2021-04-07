
from ImageProcessor import ImageProcessor
from matplotlib import pyplot
from PIL import Image
from numpy import zeros, uint8, arange

class ColorFilter:

    @staticmethod
    def invert(array):
        """
        Takes a NumPy array of an image as an argument and returns an array with inverted color.
        Authorized functions: None
        Authorized operator: -
        """
        # Maximum intensity value of the color mode
        new_array = 255 - array
        for i in range(3, len(array[0][0])):
            new_array[:, :, i] = array[:, :, i]
        return new_array

    @staticmethod
    def to_blue(array):
        """
        Takes a NumPy array of an image as an argument and returns an array with a blue filter.
        Authorized functions: .zeros, .shape
        Authorized operator: None
        """
        blue = zeros(array.shape, dtype=uint8)
        # r,g,b = array
        blue[:, :, 2] = array[:, :, 2]
        for i in range(3, len(array[0][0])):
            blue[:, :, i] = array[:, :, i]
        return blue

    @staticmethod
    def to_green(array):
        """
        Takes a NumPy array of an image as an argument and returns an array with a green filter.
        Authorized functions: None
        Authorized operator: *
        """
        green = zeros(array.shape, dtype=uint8)
        # r,g,b = array
        green[:, :, 1] = array[:, :, 1]
        for i in range(3, len(array[0][0])):
            green[:, :, i] = array[:, :, i]
        return green

    @staticmethod
    def to_red(array):
        """
        Takes a NumPy array of an image as an argument and returns an array with a red filter.
        Authorized functions : to_green, to_blue
        Authorized operator: -, +
        """
        # call to_green ot to_blue use to_green.__func__
        red = zeros(array.shape, dtype=array.dtype)
        # r,g,b = array
        red[:, :, 0] = array[:, :, 0]
        for i in range(3, len(array[0][0])):
            red[:, :, i] = array[:, :, i]
        return red

    @staticmethod
    def to_celluloid(array):
        """
        Takes a NumPy array of an image as an argument, and returns an array with a celluloid shade filter.
        The celluloid filter must display at least four thresholds of shades.
        Be careful! You are not asked to apply black contour on the object here
        (you will have to, but later...), you only have to work on the shades of your images.
        Authorized functions: arange, linspace
        """

        for i in range(2):
            array[array[:, :, i] <= 64, 0] = 0
            array[((array <= 128) & (array > 64))[:, :, i], 0] = 64
            array[array[:, :, i] > 128, 0] = 128
        return array


imp = ImageProcessor()
arr = imp.load("gg.png")

cf = ColorFilter()

#
# ImageProcessor.display(arr)

newarry = cf.invert(arr)
ImageProcessor.display(newarry)
# x = ImageProcessor()
#
# a = ImageProcessor.load("42AI.png")
# print(a)
#
# ImageProcessor.display(a)

#
# r, g, b = arr
# ImageProcessor.display(r)
# ImageProcessor.display(g)
# ImageProcessor.display(b)

newarry2 = cf.to_blue(arr)
ImageProcessor.display(newarry2)
#
newf = cf.to_green(arr)
ImageProcessor.display(newf)

newf0 = cf.to_red(arr)
ImageProcessor.display(newf0)

newf01 = cf.to_celluloid(arr)
ImageProcessor.display(newf01)


