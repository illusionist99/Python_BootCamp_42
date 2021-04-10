
import random
import numpy
import time
import matplotlib.pyplot as plt


class KmeansClustering:
    def __init__(self, max_iter=20, ncentroid=3):
        self.ncentroid = ncentroid  # number of centroids
        self.max_iter = max_iter  # number of max iterations to update the centroids
        self.centroids = []  # values of the centroids

    def fit(self, X):
        """
        Run the K-means clustering algorithm.
        For the location of the initial centroids, random pick ncentroids from the dataset.
        Args:
          X: has to be an numpy.ndarray, a matrice of dimension m * n.
        Returns:
          None.
        Raises:
          This function should not raise any Exception.
        """
        (x, y) = X.shape
        print(x, y)
        for i in range(self.ncentroid):
            t0 = random.randrange(x)
            t1 = random.randrange(y)
            print(t0, t1)
            self.centroids.append(array[t0][t1])

        plt.plot(array, linestyle=' ', marker='o')
        plt.plot(self.centroids, linestyle=' ', marker='o')
#         d = {}
#         f = 0
#         for i in self.centroids:
#             d["centroid_{}".format(f)] = []
#             f += 1
#
#         # print(d)
#         # exit()
#         j = 0
#         i = 0
#         k = 0
#         print(len(array))
#         while k < len(self.centroids):
#             j = 0
#             while j < len(array):
#                 i = 0
#                 while i < len(array[j]):
#                     dist = (self.centroids[k][1] - i) ** 2 + (self.centroids[k][0] - j) ** 2
#                     d["centroid_{}".format(k)].append(numpy.sqrt(dist))
#                     i += 1
#                 j += 1
#             k += 1
#         print(d)
#         i = 0
#         j = 0
#         k = 0
#         while i < len(array[j]):
#             k = 0
#             while k < len(self.centroids):
#                 if
#     #     Assign closest point to closest cluster








    def predict(self, X):
        """
        Predict from wich cluster each datapoint belongs to.
        Args:
          X: has to be an numpy.ndarray, a matrice of dimension m * n.
        Returns:
          the prediction has a numpy.ndarray, a vector of dimension m * 1.
        Raises:
          This function should not raise any Exception.
        """
        pass


array = numpy.zeros((10, 5))

h = KmeansClustering().fit(array)
# print(h)

# color = (random.randrange(1, 255)/ 255, random.randrange(1, 255)/ 255, random.randrange(1, 255)/ 255)

plt.show()

plt.close()
