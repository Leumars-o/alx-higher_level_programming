#!/usr/bin/python3
"""
Printing of an inherited list

Classes:
    - MyList: a class that defines lists
"""


class MyList(list):
    """
    A class that defines lists

    Methods:
        - print_sorted: A method that prints a sorted list

    Return:
        - None (Prints a sorted list)
    """
    def print_sorted(self):
        """
        A method that sorts and prints the list
        """
        a = sorted(self)
        print(a)
