#!/usr/bin/python3
"""A module that provides a function that says your name
"""


def say_my_name(first_name, last_name=""):
    """A function that says your name

    Args:
        first_name (str): your first name
        last_name (str, optional): Your last name. Defaults to "".
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
