#!/usr/bin/python3
"""An intger addition function"""


def add_integer(a, b=98):
    """function takes 1 to 2 arguments, and gets the sum.

    Arguments:
        - @a: first integer variable
        - @b: second integer variable. By default, 98

    Return:
        - The integer addition of a and b
            * On Return, Additon result is typecasted
            to an int if they are float.

    raises:
        TypeError: If either of a or b is a non-integer and non-float.
    """
    if not (isinstance(a, int) or isinstance(a, float)):
        raise TypeError("a must be an integer")
    if not (isinstance(b, int) or isinstance(b, float)):
        raise TypeError("b must be an integer")
    result = a + b
    return int(result)
