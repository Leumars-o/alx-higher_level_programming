#!/usr/bin/python3
"""A module that provides a function that appends args to a json file
"""
import sys
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file


def append_args():
    """A function that adds all arguments to a python list and saves
    them to a file

    Returns:
        list: list of all arguments
    """
    filename = 'add_item.json'
    arg_list = sys.argv[1:]
    try:
        json_list = load_from_json_file(filename)
    except FileNotFoundError:
        json_list = []
    for arg in arg_list:
        json_list.append(arg)
    save_to_json_file(json_list, filename)
    return json_list
