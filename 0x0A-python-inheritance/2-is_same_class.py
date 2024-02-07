#!/usr/bin/python3
"""A function that checks if an object is exactly an instance of a class

    Functions:
        - is_same_class
"""


def is_same_class(obj, a_class):
    """
    Args:
        @obj: Object to be compared to a class
        @a_class: a class which will be checked if the object is an instance of

    Return:
        - True: if True
        - False: Otherwise
    """
    return type(obj) == a_class
