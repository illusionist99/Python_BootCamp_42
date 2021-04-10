from pandas import DataFrame
from FileLoader import FileLoader

def youngestFellah(df, year):
    """
    Write a function youngestFellah that takes two arguments:
    • a pandas.DataFrame which contains the dataset
    • an Olympic year.
    The function returns a dictionary
    containing the age of the youngest woman and man who took part in the
    Olympics on that year. The name of the dictionary’s keys is up to you,
    but it must be self-explanatory.
    """
    dictionary = {}
    if not isinstance(df, DataFrame):
        exit("What are You given me as DataFrame !!")

    mini_df = df.get(["Year", "Sex", "Age"])
    # float('inf')  Biggest number :)
    youngest_female = float('inf')
    youngest_male = float('inf')
    for yearV, sex, age in mini_df.to_numpy():
        if yearV == year:

            if sex == 'M' and age < youngest_male:
                youngest_male = age
            if sex == 'F' and age < youngest_female:
                youngest_female = age
    dictionary['f'] = youngest_female
    dictionary['m'] = youngest_male
    return dictionary


loader = FileLoader()

data = loader.load('athlete_events.csv')
d = youngestFellah(data, 2004)
print(d)
