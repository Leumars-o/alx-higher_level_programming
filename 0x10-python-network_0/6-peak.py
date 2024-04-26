#!/usr/bin/python3
"""This module contains a 'find_peak' function."""


def find_peak(list_of_integers):
    """function that finds a "Peak" in a list of unsorted integers

    Args:
        list_of_integers (list): a list of unsorted integers

    Returns:
        int: the peak value, or None if list is empty
    """

    if not list_of_integers:
        return None
    numbers = sorted(list_of_integers)
    return numbers[-1]
