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

    def to_json(self):
        """A method that returns a dict representation of
        a Student instance

        Returns:
            dict
        """
        return self.__dict__
