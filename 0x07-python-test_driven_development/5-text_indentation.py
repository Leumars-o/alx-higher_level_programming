#!/usr/bin/pyhton3
def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    special_chars = ('.', '?', ':')
    for character in text:
        if character in special_chars:
            print(character)
            print()
        else:
            print(character, end="")
