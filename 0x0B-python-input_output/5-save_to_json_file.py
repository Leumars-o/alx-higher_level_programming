#!/usr/bin/python3
"""A module that provides a function to write an object to a text file
"""
import json


def save_to_json_file(my_obj, filename):
    """A function that writes an object to a text file, using
    Json representation

    Args:
        my_obj (any): Object to be written as JSON
        filename (str): Path to file to be written
    """
    json_data = json.dumps(my_obj)
    with open(filename, mode='w', encoding='utf8') as file:
        file.write(json_data)
