# Testing ofc XD

from functools import reduce


def ft_reduce(function_to_apply, list_of_inputs):
    """
    The reduce() function accepts a function and a sequence and returns a single value calculated as follows:

    Initially, the function is called with the first two items from the sequence and the result is returned.
    The function is then called again with the result obtained in step 1 and the next value in the sequence.
    This process keeps repeating until there are items in the sequence.
    """
    if not callable(function_to_apply):
        exit("First param should be a Function")
    try:
        object_iter = iter(list_of_inputs)
    except TypeError:
        exit("Second Argument must be iterable")
    rt = 0
    if len(list_of_inputs) == 1:
        return list_of_inputs[0]
    for i in range(0, len(list_of_inputs), 2):
        try:
            rt += function_to_apply(list_of_inputs[i], list_of_inputs[i + 1])
        except IndexError:
            rt = function_to_apply(list_of_inputs[i], rt)
        # Debug Operation
        # print("{} = {} + {}".format(rt, list_of_inputs[i], list_of_inputs[i + 1]))
    return rt


def do_sum(x1, x2):
    return x1 + x2


lst = [1, 2, 3]

print(ft_reduce(do_sum, lst))

print(reduce(do_sum, lst))
