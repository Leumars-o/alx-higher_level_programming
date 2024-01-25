#!/usr/bin/python3
"""A function that divides 2 integers and prints the result.

Parameters:
    @a: Integer 1
    @b: Integer 2
Return:
    - The value of the division
    - None, otherwise
Description:
    - we assume a and b are integers
    - use of try: / except: / finally:
    - Module imports are not allowed
"""


def safe_print_division(a, b):
    division = None
    try:
        division = int(a) / int(b)
    except (ValueError, ZeroDivisionError):
        return None
    finally:
        print("Inside result: {}".format(division))
    return division
