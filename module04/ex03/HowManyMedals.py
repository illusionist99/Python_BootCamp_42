from FileLoader import FileLoader


def howManyMedals(df, participant_name):

    dictionary = {}
    mini_df = df.get(["Name", "Medal", "Year"])
    for name, medal, year in mini_df.to_numpy():
        if name == participant_name and medal != 'nan':
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
d = howManyMedals(df, 'Kjetil Andr Aamodt')
print(d)

