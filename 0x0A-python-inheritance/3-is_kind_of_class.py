#!/usr/bin/python3
"""
This module defines a function, `is_kind_of_class`, that checks if an object
is an instance of a specific class
"""


def is_kind_of_class(obj, a_class):
    """
    Function to check if an object is an instance of a given class

    Args:
        @obj: The object to check
        @a_class: The class to be compared to

    Return:
        True: if the object is an instance of the class
        False: Otherwise
    """
    return (isinstance(obj, a_class))
