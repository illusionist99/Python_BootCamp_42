t = (3, 30, 2019, 9, 25)

hour = str(t[0]).zfill(2)
minutes = str(t[1]).zfill(2)
year = str(t[2]).zfill(4)
month = str(t[3]).zfill(2)
day = str(t[4]).zfill(2)

print("{month}/{day}/{year} {hour}:{minutes}".format(month=month, day=day, year=year, hour=hour, minutes=minutes))