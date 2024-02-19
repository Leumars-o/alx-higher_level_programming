#!/usr/bin/python3
"""A module that provides a funtion that prints a formatted
text
"""


def text_indentation(text):
    """A function that prints a text with 2 new lines
    after each of these characters: '.', '?' and ':'

    Args:
        text (str): string to format
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    special_chars = ('.', '?', ':')

    for i, character in enumerate(text):
        if i == 0 and character == " ":
            continue

        elif character == " " and (
            text[i - 1] in special_chars or text[i - 1] == " "
        ):
            continue

        if character in special_chars:
            print(character)
            print()
        else:
            print(character, end="")
