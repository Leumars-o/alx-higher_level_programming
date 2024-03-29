#!/usr/bin/python3
"""Creation and usage of a square

A module that creates a class Square.

Classes:
    Square: this defines the square class

Description:
    No modules should be imported
"""


class Square:
    """A class that defines a square

    Methods:
        - __init__: Method initializes the square class
        _ area: calculates the area of the square
    """
    def __init__(self, size=0):
        """A method that initializes the square class
        sets '__size' to 'size' if argument is valid

        Return:
            - None
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        """A getter property for the size attribute

        Return:
            - value of size in the instance
        """
        return (self.__size)

    @size.setter
    def size(self, value=None):
        """A property that sets the value of size

        Args:
            - value: value to be set to size
                * by default is None
                * must be an integer
                * must be greater than 0
        """
        if value is None:
            return
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """A method that calculates the area of a square.

        Attributes:
            - None
        Return:
            - returns the area of the squre
        """
        return (self.__size ** 2)
