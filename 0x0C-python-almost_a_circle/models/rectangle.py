#!/usr/bin/python3
"""A module that defines a cRectangle subclass

Classes:
    Rectangle: A class that defines and creates rectangles with 'Base'
    as its Superclass
"""
from .base import Base


class Rectangle(Base):
    """A Rectangle subclass from Base class that defines and creates Rectangles

    Args:
        Base (Superclass)

    Methods:
        __init__: initalization method
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """A rectangle initializing method

        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle
            x (int, optional): Defaults to 0.
            y (int, optional): Defaults to 0.
            id (int, optional): id of the rectangle. Defaults to None.
        """
        super().__init__(id)
        if type(width) != int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        if type(height) != int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        if type(x) != int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        if type(y) != int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """A method that returns the area of a Rectangle

        Returns:
            int: Area of Rectangle
        """
        return (self.__width * self.__height)

    def display(self):
        """A method that prints a representation of the Rectangle
        with '#' character
        """
        for j in range(self.__y):
            print()
        for i in range(self.height):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        """A __str__ method that returns a string with information
        about the rectangle

        Returns:
            str: A string that describes the parameters of the Rectangle
        """
        string = f"[Rectangle] ({self.id}) {self.__x}/{self.__y} " \
            f"- {self.__width}/{self.__height}"
        return string

    def update(self, *args, **kwargs):
        """A method that updates the Rectangle using *args and **kwargs
        functions

        Args:
            @args: a tuple of elements to be passed into the Rectangle
            @kwargs: a Dictionary of elements to be passed to the rectangle
        """
        attributes = ['id', 'width', 'height', 'x', 'y']
        if args and len(args) != 0:
            for i, arg in enumerate(args):
                if i < len(attributes):
                    if i == 0 and arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        setattr(self, attributes[i], arg)
        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key in attributes:
                    if key == 'id' and value is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        setattr(self, key, value)
