#!/usr/bin/python3
# function that finds a "Peak" in a list of unsorted integers
def find_peak(list_of_integers):
    numbers = list_of_integers
    try:
        return(max(numbers))
    except ValueError:
        return None
