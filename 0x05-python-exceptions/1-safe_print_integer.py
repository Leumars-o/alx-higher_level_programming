#!/usr/bin/python3
"""A function that safely prints an integer list.

Parameters:
    @value: Integer variable to safely print
Return:
    True: If value is printed sucessfully
    False: Otherwise
Description:
    - value can be any type (integer, string, etc.)
    - The integer should be printed followed by a new line
    - You have to use try: / except:
    - You have to use "{:d}".format() to print as integer
    - You are not allowed to import any module
    - You are not allowed to use type()
"""


def safe_print_integer(value):
    try:
        print("{:d}".format(value))
        return True
    except (TypeError, ValueError):
        return False
