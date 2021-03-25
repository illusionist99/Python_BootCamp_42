import sys


def elementary(a, b):
    a = float(a)
    b = float(b)
    operation = a + b
    print("Sum:         " + str(int(operation)))
    operation = a - b
    print("Difference:  " + str(int(operation)))
    operation = a * b
    print("Product:     " + str(int(operation)))
    if b == 0:
        operation = "ERROR (div by zero)"
    else:
        operation = a / b
    print("Quotient:    " + str(operation))
    if b == 0:
        operation = "ERROR (modulo by zero)"
    else:
        operation = int(a % b)
    print("Remainder:   " + str(operation))


args = sys.argv[1:]
if len(args) == 0:
    print("""Usage: python operations.py <number1> <number2>
    Example:
    python operations.py 10 3""")
    exit(-1)

elif len(args) > 2:
    print("""InputError: too many arguments
    Usage: python operations.py <number1> <number2>
    Example:
    python operations.py 10 3""")
    exit(-1)

if not args[0].isdigit() or not args[1].isdigit():
    print("""InputError: only numbers
    Usage: python operations.py <number1> <number2>
    Example:
    python operations.py 10 3""")
    exit(-1)

elementary(args[0], args[1])
