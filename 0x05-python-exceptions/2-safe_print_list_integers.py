#!/usr/bin/python3
"""A function that prints the first x elements of a list and only integers.

Parameters:
    @my_list: The given List
    @x: number of elements to access in my_list
Return:
    - Prints all integers on success
    - The real number of integers printed, otherwise.
Description:
    - my_list can contain any type (integer, string, etc.)
    - All integers have to be printed on the same line followed by a new line
    - other type of value in the list must be skipped (in silence).
    - x represents the number of elements to access in my_list
    - You are not allowed to import any module
    - You are not allowed to use len()
"""


def safe_print_list_integers(my_list=[], x=0):
    count, i = 0, 0
    while i < x:
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except (TypeError, ValueError):
            pass
        i += 1
    print()
    return count
