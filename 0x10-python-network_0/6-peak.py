#!/usr/bin/python3
# function that finds a "Peak" in a list of unsorted integers


def find_peak(list_of_integers):
    if not list_of_integers:
        return None
    numbers = sorted(list_of_integers)
    try:
        return numbers[-1]
    except (ValueError, IndexError):
        return None
