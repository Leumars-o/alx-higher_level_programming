#!/usr/bin/python3
"""A module that provides a student defining class
"""


class Student:
    """A class `Student` that defines and creates students
    """
    def __init__(self, first_name, last_name, age):
        """A method that initializes the Student class

        Args:
            first_name (str): students first name
            last_name (str): students last name
            age (int): students age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """A method that returns a dict representation of
        a Student instance

        Returns:
            dict
        """
        if isinstance(attrs, list):
            for item in attrs:
                if isinstance(item, str):
                    return {
                        k: getattr(self, k) for k in attrs if hasattr(self, k)
                        }
        else:
            return self.__dict__

    def reload_from_json(self, json):
        """A method that replaces all attributes of Student

        Args:
            json (dict): key/value pair dict to replace attributes with
        """
        for key, value in json.items():
            setattr(self, key, value)
