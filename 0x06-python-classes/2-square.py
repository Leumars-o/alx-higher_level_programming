#!/usr/bin/python3
"""A module that defines a Square class

Attributes:
    - Square: Square class
"""


class Square:
    """A class that defines a square

    Attributes:
        - size: Instance attribute, with default = 0
            * must be an int
            * must be greater than 0
    """
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
