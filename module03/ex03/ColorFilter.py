
from ImageProcessor import ImageProcessor
from matplotlib import pyplot
from PIL import Image
import numpy

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
        return new_array

    @staticmethod
    def to_blue(array):
        """
        Takes a NumPy array of an image as an argument and returns an array with a blue filter.
        Authorized functions: .zeros, .shape
        Authorized operator: None
        """
        blue = array

        blue[:, :, 1] = 0
        blue[:, :, 0] = 0
        return blue

    @staticmethod
    def to_green(array):
        """
        Takes a NumPy array of an image as an argument and returns an array with a green filter.
        Authorized functions: None
        Authorized operator: *
        """
        pass

    @staticmethod
    def to_red(array):
        """
        Takes a NumPy array of an image as an argument and returns an array with a red filter.
        Authorized functions : to_green, to_blue
        Authorized operator: -, +
        """
        pass

    @staticmethod
    def to_celluloid(array):
        """
        Takes a NumPy array of an image as an argument, and returns an array with a celluloid shade filter.
        The celluloid filter must display at least four thresholds of shades.
        Be careful! You are not asked to apply black contour on the object here
        (you will have to, but later...), you only have to work on the shades of your images.
        Authorized functions: .arange, linspace
        """
        pass


imp = ImageProcessor()
arr = imp.load("42AI.png")

# cf = ColorFilter()
# newarry = cf.invert(arr)
ImageProcessor.display(arr)
# x = ImageProcessor()
#
# a = ImageProcessor.load("42AI.png")
# print(a)
#
# ImageProcessor.display(a)


# inverted_img = Image.fromarray((newarry * 255).astype(numpy.uint8))
#
# newarry2 = cf.to_blue(arr)
# inverted_img = Image.fromarray((newarry2).astype(numpy.uint8))


