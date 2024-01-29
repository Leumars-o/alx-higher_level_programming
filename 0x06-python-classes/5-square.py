#!/usr/bin/python3
"""creation and usage of squares
A module that creates a square class

Classes:
    - Square: A class that defines squares
"""


class Square:
    """A class that creates squares

    Methods:
        __init__: Initializes the square class
        area: calculates the area of the square
        my_print: prints out a representation of the square using '#'
    """
    def __init__(self, size=0):
        """A method that initializes the square class

        Attributes:
        - size: integer value, size of square
            * default value is 0
            * must be greater than 0
            * must be an integer
        """
        if not isinstance(size, int):
            raise TypeError("size must be an intger")
        if size < 0:
            raise ValueError(" size must be >= 0")
        self.__size = size

    @property
    def size(self):
        """Property that retrieves the size value

        Return:
            size of square in an instance
        """
        return self.__size

    @size.setter
    def size(self, value):
        """property setter, assigns a value to size

        Attribute:
            - value: value to be assigned as size
                * value must be an integer
                * must be greater than 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an intger")
        if value < 0:
            raise ValueError(" size must be >= 0")
        self.__size = value

    def area(self):
        """Method that calculates the area of the square

        Return:
            - area of square
        """
        return (self.__size ** 2)

    def my_print(self):
        """Method that prints a square to stdout with '#'
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print("#" * self.__size)
