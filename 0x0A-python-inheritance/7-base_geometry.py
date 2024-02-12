#!/usr/bin/python3
"""
A module that defines a class `BaseGeometry`

Classes:
    -BaseGeometry
"""


class BaseGeometry:
    """
    A class that defines and creates BaseGeometry

    Methods:
        area: raises an exception when called
        integer_validator
    """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
        self.value = value
        self. name = name
