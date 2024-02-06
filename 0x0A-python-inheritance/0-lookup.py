#!/usr/bin/python3
"""
A function that returns a list of available attributes and methods of an object

Args:
    @obj: The object its attributes is to be returned
"""


def lookup(obj):
    return dir(obj)
