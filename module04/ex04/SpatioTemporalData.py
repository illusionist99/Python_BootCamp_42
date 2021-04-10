from FileLoader import FileLoader

class SpatioTemporalData:

    def __init__(self, df):
        self.mini_df = df.get(["Year", "City"])

    def when(self, location):
        lst = []
        for year, city in self.mini_df.to_numpy():
            if city == location and year not in lst:
                lst.append(year)
        return lst

    def where(self, date):
        lst = []
        for year, city in self.mini_df.to_numpy():
            if date == year and city not in lst:
                lst.append(city)
        return lst


df = FileLoader.load('../data/athlete_events.csv')
d = SpatioTemporalData(df)
print(d.when('Paris'))