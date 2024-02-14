#!/usr/bin/python3
"""
A module that defines a class `BaseGeometry`

Classes:
    -BaseGeometry
"""


class BaseGeometry:
    """
    A class that defines and creates Geometric shapes

    Methods:
        area: raises an exception when called
        integer_validator
    """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
        self.value = value
        self. name = name


class Rectangle(BaseGeometry):
    """A class `Rectangle that inherits from `BaseGeometry`

    Args:
        BaseGeometry (class): Superclass that defines and creates
        Geometric shapes

    Methods:
        - __init__: intialization method
    """
    def __init__(self, width, height):
        """A method that initializes the Rectangle class

        Args:
            width (int): the width of the rectangle
            height (int): the height of the rectangle
        """
        BaseGeometry.integer_validator(self, 'width', width)
        BaseGeometry.integer_validator(self, 'height', height)
        self.__width = width
        self.__height = height
