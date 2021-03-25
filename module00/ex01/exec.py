import sys

args = sys.argv[1:]
args.reverse()
displayed = ""

for word in args:
    for letter in word[::-1]:
        if letter.islower():
            displayed += letter.upper()
        elif letter.isupper():
            displayed += letter.lower()
        else:
            displayed += letter
    if word != args[-1]:
        displayed += ' '

print(displayed)
