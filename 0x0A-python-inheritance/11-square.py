#!/usr/bin/python3
"""
A module that defines a class `Square`

Classes:
    - Square
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A class `Rectangle that inherits from `BaseGeometry`

    Args:
        BaseGeometry (class): Superclass that defines and creates
        Geometric shapes

    Methods:
        - __init__: intialization method
        - area: calculates the area of the square
    """
    def __init__(self, size):
        """A method that initializes the square class

        Args:
            size (int): the width of the square
        """
        self.integer_validator('size', size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Method that returns the area of the square

        Returns:
            int: The area of the square
        """
        return self.__size ** 2

    def __str__(self):
        """
        string method that returns a description of the rectangle
        """
        string = f"[Square] {self.__size}/{self.__size}"
        return string
