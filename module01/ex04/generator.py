import random


def generator(text, seq=" ", option=None):
    for arg in text.split(seq):
        yield arg


print(list(generator(input())))
