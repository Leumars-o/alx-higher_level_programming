#!/usr/bin/python3
"""
A module that defines a class `BaseGeometry`

Methods:
    - None
"""


class BaseGeometry:
    """
    A class that defines and creates BaseGeometry

    Methods:
        area: raises an exception when called
    """
    def area(self):
        raise Exception("area() is not implemented")
