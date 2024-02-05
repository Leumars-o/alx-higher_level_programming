#!/usr/bin/python3
"""
This module defines the Rectangle class

Classes:
    - Rectangle: Defines a rectangle
"""


class Rectangle:
    """This class defines a rectangle

    Methods:
        - __init__: Initializes a Rectangle object with optional
        width and height
    """
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        Rectangle.number_of_instances += 1
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """
        Public Method that calculates the area of a Rectangle

        Return:
            - Area of rectangle
        """
        return (self.__height * self.__width)

    def perimeter(self):
        """
        Public Method that calculates the perimeter of a rectangle

        Return:
            - Perimeter of a rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return ((self.__height * 2) + (self.__width * 2))

    def __str__(self):
        """
        A method that defines the string representation of a rectangle

        Return:
            - Returns a rectangle with size self.__width & self.__height
            represented by '#' character
        """
        if self.__width == 0 or self.__height == 0:
            return ("")
        else:
            rect = ""
            for i in range(self.__height):
                if i != self.__height - 1:
                    rect += '#' * self.__width + '\n'
                else:
                    rect += '#' * self.__width
            return rect

    def __repr__(self):
        """
        A method that recreates a string representation of a new instance

        Return:
            - Returns a string representation of the rectangle instance
        """
        return ("Rectangle({}, {})".format(self.__width, self.__height))

    def __del__(self):
        """
        A method that prints a message when an instance of Rectangle is deleted

        Return:
            - None
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
