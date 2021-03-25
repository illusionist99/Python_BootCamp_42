import string
import sys


def get_input():
    text = ""
    print("What is the text to analyze")
    for line in sys.stdin:
        text += line
    return text


def text_analyzer(*text):
    """    * This function is useless but it can count the number of
    * upper characteres, lower characteres, punctuation and spaces in a given text"""
    num = len(text)
    if num > 1:
        print("ERROR")
        exit(-1)
    elif num == 0:
        text = None
    if text is None:
        text = get_input()
    upper_cases = 0
    lower_cases = 0
    punctuation = 0
    spaces = 0
    rcx = 0
    while rcx < len(text):
        if text[rcx].isspace():
            spaces += 1
        if text[rcx].isupper():
            upper_cases += 1
        if text[rcx].islower():
            lower_cases += 1
        if text[rcx] in string.punctuation:
            punctuation += 1
        rcx += 1
    print("The text contains " + str(spaces + upper_cases + punctuation) + " characters:")
    print("- " + str(upper_cases) + " upper letters")
    print("- " + str(lower_cases) + " lower letters")
    print("- " + str(punctuation) + " punctuation marks")
    print("- " + str(spaces) + " spaces")

#text_analyzer()
#print(text_analyzer.__doc__)
