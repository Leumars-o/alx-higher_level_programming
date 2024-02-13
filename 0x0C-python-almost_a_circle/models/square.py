#!/usr/bin/python3
"""A module that defines a Square subclass

Classes:
    Square: A class that defines and creates Squares with 'Rectangle'
    as its Superclass
"""
from .rectangle import Rectangle


class Square(Rectangle):
    """A Square subclass from Rectangle class that defines and creates Squares

    Args:
        Rectangle (Superclass)

    Methods:
        - __init__: initalization method
        - __str__: Prints a string with information about the square
    """
    def __init__(self, size, x=0, y=0, id=None):
        """A Square initializing method

        Args:
            size (int): size of the square
            x (int, optional): Defaults to 0.
            y (int, optional): Defaults to 0.
            id (int, optional): id of the square. Defaults to None.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """A __str__ method that returns a string with information
        about the square

        Returns:
            str: A string that describes the parameters of the Square
        """
        string = f"[Square] ({self.id}) {self.x}/{self.y} " \
            f"- {self.width}"
        return string

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
