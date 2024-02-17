#!/usr/bin/python3
"""A module that provides a function that returns a dictionary
description
"""


def class_to_json(obj):
    """A function that returns the dictionary desc with
    simple data structure for json serialization of an object

    Args:
        obj (ant):  (list, dictionary, string, integer and boolean)

    Returns:
        dict
    """
    return obj.__dict__
