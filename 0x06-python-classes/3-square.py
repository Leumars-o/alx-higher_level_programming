#!/usr/bin/python3
"""A module that creates a class, Square.

Attributes:
    - Square: a class that creates squares
"""


class Square:
    """A class that defines a square

    Methods:
        - __init__: initializes the class
        - area: calculates the area of the square
    """
    def __init__(self, size=0):
        """A method that initializes the square class

        Attributes:
            - size: an instance attribute that defines the size of the square
                * default value is 0
                * size must be an integer
                * value of size must be greater than 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """A method 'area' that defines the area of a square

        Arguments:
            - none
        Return:
            - returns the area of the square
        """
        return(self.__size ** 2)
