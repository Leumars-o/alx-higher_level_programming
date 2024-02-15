#!/usr/bin/python3


def write_file(filename="", text=""):
    """A function that writes a string to a text file

    Args:
        filename (str, optional): _description_. Defaults to "".
        text (str, optional): _description_. Defaults to "".

    Returns:
        int: Returns the number of characters written
    """
    with open(filename, mode='w', encoding='utf8') as f:
        f.write(text)
        return f.tell()
