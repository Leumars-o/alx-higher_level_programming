#!/usr/bin/python3
"""A module that defines a class `Base`

Classes:
    Base: base class that manages 'id' attributes
"""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """A method for sharing data representation using JSON

        Args:
            list_dictionaries (list): A list of dictionaries

        Returns:
            dict: A JSON string representation of list_dictionaries
        """
        if list_dictionaries is None or list_dictionaries == "[]":
            return "[]"
        json_data = json.dumps(list_dictionaries)
        return json_data

    @classmethod
    def save_to_file(cls, list_objs):
        """A class method that writes the JSON string representation
        of list_objs to a file

        Args:
            list_objs (list): a list of instances
        """
        filename = cls.__name__ + ".json"
        with open(filename, 'w') as file:
            if list_objs is None:
                file.write("[]")
            else:
                new_dict = Base.to_json_string(
                    [obj.to_dictionary() for obj in list_objs]
                    )
                file.write(new_dict)

    @staticmethod
    def from_json_string(json_string):
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)
