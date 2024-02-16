#!/usr/bin/python3
"""A module that provides a function that decodes a JSON string
"""
import json


def from_json_string(my_str):
    """A function that decodes a JSON string to an object
    (Python data structure)

    Args:
        my_str (str): JSON string to be decoded

    Returns:
        dict: Python dictionary
    """
    new_string = json.loads(my_str)
    return new_string
