import sys

args = sys.argv[1:]
num = 0
if len(args) == 1 and args[0].isdigit():
    num = int(args[0])
    if (num == 0):
        print "I'm Zero."
    elif num % 2 == 0:
        print "I'm Odd."
    else:
        print "I'm Even."
else :
    print "ERROR"
