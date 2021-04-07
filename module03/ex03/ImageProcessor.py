# load and display an image with Matplotlib
from matplotlib import image
from matplotlib import pyplot
from numpy import asarray, uint8

class ImageProcessor:
    @staticmethod
    def load(path):
        # load image as pixel array
        img = image.imread(path)

        # convert image to numpy array
        array = asarray(img)
        array = (array * 255).astype(uint8)

        print("Loading image of dimensions {} * {} and shape : {}".format(img.shape[0], img.shape[1], array.shape))
        return array

    @staticmethod
    def display(array):
        # draw image
        pyplot.imshow(array)
        # show image
        pyplot.show()
        return

# x = ImageProcessor()
#
# a = ImageProcessor.load("42AI.png")
# print(a)
#
# ImageProcessor.display(a)
