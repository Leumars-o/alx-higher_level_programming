#!/usr/bin/python3
"""A module that creates squares

Classes:
    - Square: A class that defines squares
"""


class Square:
    """A class that defines squares

    Methods:
        __init__: initializes the square class
        area: calculates the area of the square
        my_print: prints out a formatted square
    """
    def __init__(self, size=0, position=(0, 0)):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        if isinstance(position, tuple) and len(position) == 2:
            for element in position:
                if isinstance(element, int) and element >= 0:
                    self.__position = position
                else:
                    raise TypeError
                    ("position must be a tuple of 2 positive integers")
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    @property
    def size(self):
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return (self.__position)

    @position.setter
    def position(self, value):
        if isinstance(value, tuple) and len(value) == 2:
            for element in value:
                if isinstance(element, int) and element >= 0:
                    self.__position = value
                else:
                    raise TypeError
                    ("position must be a tuple of 2 positive integers")
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """A method that calculates the area of a square

        Attributes:
            - None
        Return:
            - Area of the square
        """
        return (self.__size ** 2)

    def my_print(self):
        """A method that prints a formatted square

        Attributes:
            - None
        """
        if self.__size == 0:
            print()
        else:
            if self.__position[1] > 0:
                print('\n' * self.__position[1], end="")
            for i in range(self.__size):
                print(' ' * self.__position[0] + "#" * self.__size)
