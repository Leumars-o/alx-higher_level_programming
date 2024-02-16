#!/usr/bin/python3
"""A module that provides a function that creates an object
from a json file
"""
import json


def load_from_json_file(filename):
    """A function that creates a JSON object from a JSON file

    Args:
        filename (str): path to json file

    Returns:
        object from the json file
    """
    with open(filename, encoding='utf8') as file:
        json_data = file.read()
        new_data = json.loads(json_data)
    return new_data
