#!/usr/bin/python3
"""A module that provides a function to print a square
"""


def print_square(size):
    """A function that prints a square with the character '#'

    Args:
        size (int): size of the square to be printed
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    for i in range(size):
        print("#" * size)
