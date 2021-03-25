phrase = "The right format"


if len(phrase) > 42:
    phrase = phrase[:41]

print("-" * (42 - len(phrase)) + "{phrase:>}".format(phrase=phrase), end='')
