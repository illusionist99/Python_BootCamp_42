from FileLoader import FileLoader


def howManyMedalsByCountry(df, country_name):
    dictionary = {}
    mini_df = df.get(["Team", "Medal", "Year"])
    mini_df.drop_duplicates()
    for team, medal, year in mini_df.to_numpy():
        if country_name == team and medal != 'nan':
            if not year in dictionary.keys():
                dictionary[year] = {
                    'G': 0,
                    'S': 0,
                    'B': 0
                }
            if medal == 'Silver':
                dictionary[year]['S'] += 1
            elif medal == 'Bronze':
                dictionary[year]['B'] += 1
            elif medal == 'Gold':
                dictionary[year]['G'] += 1
    return dictionary


df = FileLoader.load('../data/athlete_events.csv')
d = howManyMedalsByCountry(df, 'China')
print(d)
