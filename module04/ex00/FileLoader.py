from pandas import DataFrame, read_csv

class FileLoader:
    @staticmethod
    def load(path):
        """
        takes as an argument the file path of the dataset to load,
        displays a message specifying the dimensions of
        the dataset (e.g. 340 x 500) and returns the dataset
        loaded as a pandas.DataFrame.
        """
        try:
            df = read_csv(path)
        except FileNotFoundError:
            exit("Error In File Path")
        return df

    @staticmethod
    def display(df, n):
        """
        takes a pandas.DataFrame and an integer as arguments,
        displays the first n rows of the dataset if n is positive,
        or the last n rows if n is negative.
        """
        if n >= 0:
            print(df.head(n))
        elif n < 0:
            print(df.tail(-n))

df = FileLoader.load("trees.csv")
FileLoader.display(df, 3)
