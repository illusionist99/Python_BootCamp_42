
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
        plt.plot(array, linestyle=' ', marker='o')
        (x, y) = X.shape
        for i in range(self.ncentroid):
            t0 = random.randrange(y)
            t1 = random.randrange(y)
            plt.plot(t0, t1, linestyle=' ', marker='o')
            self.centroids.append((t0, t1))

        j = 0
        distance = []
        k_distances = []
        while j < y:
            i = 0
            while i < x:
                for (x0, y0) in self.centroids:
                    distance.append(((x0 - i) ** 2 + (y0 - y) ** 2) ** 0.5)
                i += 1
            j += 1


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
