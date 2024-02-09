#!/usr/bin/python3
"""
Defines a locked class
"""


class LockedClass:
    """
    A class that Prevents the intialization of a new attribute
    other than 'first_name'.
    """
    __slots__ = ["first_name"]
