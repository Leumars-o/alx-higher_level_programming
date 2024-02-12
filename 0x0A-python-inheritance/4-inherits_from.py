#!/usr/bin/python3
"""
A module that defines a function `inherits_from` that checks if an
object is an instance of a class that inherited (directly or indirectly)
from the specified class
"""


def inherits_from(obj, a_class):
    """
    A function that checks if an object is an instance of a class
    that inherited (directly or indirectly) from the specified class

    Args:
        @obj: Object to check
        @a_class: The class to check against

    Return:
        -True: if the b=object is an instance of the class inherited
                directly or indirectly from the specified class
        -False: Otherwise
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class
