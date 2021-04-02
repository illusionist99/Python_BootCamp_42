def ft_map(function_to_apply, list_of_inputs):
    """
    Returns a list of the results after applying the given function
    to each item of a given iterable (list, tuple etc.)
    """
    if not callable(function_to_apply):
        exit("First param should be a Function")
    try:
        object_iter = iter(list_of_inputs)
    except TypeError:
        exit("Second Argument must be iterable")
    lst = []
    for item in list_of_inputs:
        lst.append(function_to_apply(item))
    return lst



def power_of_n(num):
    return (num + "kkk")


lol = {
        'key': "kk",
        'ff': "ez"}



print(ft_map(power_of_n, lol))
