#!/usr/bin/python3
"""A module that provides a function that appends a text into a file
"""


def append_write(filename="", text=""):
    """A function that appends a string at the end of a text file

    Args:
        filename (str, optional): path to file to be appended.
        text (str, optional): string to be appended to the file.

    Returns:
        int: number of characters appended
    """
    with open(filename, mode="a", encoding='utf8') as f:
        f.write(text)
        return f.tell()
