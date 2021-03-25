t = (0, 4, 132.42222, 10000, 12345.67)

day = str(t[0]).zfill(2)
exercise = str(t[1]).zfill(2)
number = round(t[2], 2)
num2 = format(t[3], ".2e")
num3 = format(t[4], ".2e")

print("day_{day}, ex_{exe} : {number}, {num2}, {num3}".format(day=day, exe=exercise, number=number, num2=num2, num3=num3))
