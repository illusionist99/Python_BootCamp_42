import sys
import string

args = sys.argv[1:]

foo = args[0].split(" ")

if len(args) != 2:
    print("ERROR")
    exit(-1)

if not args[1].isdigit():
    print("ERROR")
    exit(-1)
if args[0].isdigit():
    print("ERROR")
    exit(-1)

max_len = int(args[1])
display = []


def remove_punct(msg):
    rt = ""
    for letter in msg:
        if not (letter in string.punctuation):
            rt += letter
    return rt


for arg in foo:
    if len(arg) > max_len:
        display.append(remove_punct(arg))

print(display)
