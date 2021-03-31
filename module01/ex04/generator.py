import random

def shuffle(args):
    size = len(args)
    shuffled_list = []
    available = args.copy()

    for i in range(size):
        random_arg = available[random.randint(0, len(available) - 1)]
        shuffled_list.append(random_arg)
        available.remove(random_arg)

    return shuffled_list


def unique(args):
    """Function that returns unique words in a given list"""

    unique_list = []

    for arg in args:
        if arg not in unique_list:
            unique_list.append(arg)

    return unique_list


def generator(text, sep=" ", option=None):
    """Option is an optional arg, sep is mandatory"""

    if not (isinstance(text, str) and isinstance(sep, str)):
        exit("please Put Some text in arg")

    if not (option == "shuffle" or option == "unique" or option == "ordered" or option is None):
        exit("Not a Valid option !")

    content = text.split(sep)

    if option == "ordered":
        content.sort()
    elif option == "unique":
        content = unique(content)
    elif option == "shuffle":
        content = shuffle(content)
    for arg in content:
        yield arg


useless_text = "Le Lorem Ipsum est simplement du faux texte."
useless_text_2 = "Lorem Ipsum Lorem Ipsum"

for word in generator(useless_text, sep=" ", option="ordered"):
    print(word)


