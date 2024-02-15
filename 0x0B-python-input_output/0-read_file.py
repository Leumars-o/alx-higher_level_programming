#!/usr/bin/python3
"""A function that reads from a text file
"""


def read_file(filename=""):
    """Function reads a texts file and prints to stdout

    Args:
        filename (str, optional): path to file to read.
    """
    with open(filename, encoding='utf8') as f:
        print(f.read())
