#!/usr/bin/python3
"""
Attributes and methods of objects

Funtions:
    - lookup: a function that returns a list of available
    attributes of an object
"""


def lookup(obj):
    """
    a function that returns a list of available attributes and
    methods of an object

    Arguments:
        @obj: The objext its attributes is to be returned

    Return:
        - A list object
    """
    return dir(obj)
