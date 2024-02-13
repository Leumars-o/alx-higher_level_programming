#!/usr/bin/python3
"""A module that defines a class `Base`

Classes:
    Base: base class that manages 'id' attributes
"""


class Base:
    """A class that defines and manages 'id' attributes

    Methods:
        - __init__: intialization method
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialization method

        Args:
            id (_type_, int): _description_. Defaults to None.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects


class Rectangle(Base):
    """A Rectangle subclass from Base class that defines and creates Rectangles

    Args:
        Base (Superclass)

    Methods:
        __init__: initalization method
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
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
            raise TypeError("value must be an integer")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("value must be an integer")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("value must be an integer")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("value must be an integer")
        self.__y = value
