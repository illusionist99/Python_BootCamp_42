from pandas import DataFrame


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
            f = open(path, "r")
        except FileNotFoundError:
            exit("Error In File Path")
        count = 0
        lines = list(map(lambda x: x.strip().split(","), f.readlines()))
        df = DataFrame(lines)
        f.seek(0)
        for line in f:
            count += 1
        print("Loading dataset of dimensions {count} * {items}".format(count=count, items=len(line.split(","))))
        return df

    @staticmethod
    def display(df, n):
        """
        takes a pandas.DataFrame and an integer as arguments,
        displays the first n rows of the dataset if n is positive,
        or the last n rows if n is negative.
        """
        print(df.head(n))

df = FileLoader.load("athlete_events.csv")
FileLoader.display(df, 3)
