from FileLoader import FileLoader
from pandas import DataFrame

def proportionBySport(df, year, sport, gender):

    dictionary = {}
    if not isinstance(df, DataFrame):
        exit("What are You given me as DataFrame !!")
    df.drop_duplicates()
    mini_df = df.get(["Year", "Sex", "Age", "Sport"])
    count = 0
    total = 0
    mini_df.drop_duplicates(subset=['Year', 'Age', 'Sport', 'Sex'], keep=False, inplace=True)
    for yearV, sex, age, Sport in mini_df.to_numpy():
        if Sport == sport and sex == gender and yearV == year:
            count += 1
        if sex == gender and yearV == year:
            total += 1
    return count/total


df = FileLoader.load('../data/athlete_events.csv')
print(proportionBySport(df, 2004, 'Tennis', 'F'))

