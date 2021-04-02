def ft_filter(function_to_apply, list_of_inputs):
    """
    The filter() method constructs an iterator from elements
    of an iterable for which a function returns true.
    """
    if not callable(function_to_apply):
        exit("First param should be a Function")
    try:
        object_iter = iter(list_of_inputs)
    except TypeError:
        exit("Second Argument must be iterable")
    lst = []
    for item in list_of_inputs:
        if function_to_apply(item) == True: 
            lst.append(item)
    return lst



def is_positive(num):
    if num >= 0:
        return True
    return False


lol = (-9, -7, 5 , 3, 1, 0)


print(lol)
print(ft_filter(is_positive, lol))
