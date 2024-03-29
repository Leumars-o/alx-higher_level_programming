#!/usr/bin/python3
"""
A module that defines a class `BaseGeometry`

Classes:
    - BaseGeometry
    - Rectangle
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


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
