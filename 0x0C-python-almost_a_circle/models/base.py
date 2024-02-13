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
