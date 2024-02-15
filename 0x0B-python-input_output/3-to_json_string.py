#!/usr/bin/python3
"""A module that provides a function that returns
a json string
"""
import json


def to_json_string(my_obj):
    """A function that returns the JSON representation
    of an object(string)

    Args:
        my_obj (str):

    Returns:
        str: json representation of the string
    """
    return json.dumps(my_obj)
