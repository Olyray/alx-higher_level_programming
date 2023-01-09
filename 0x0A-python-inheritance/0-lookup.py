#!/usr/bin/python3
"""A function to return a list of attributes
and object.
"""


def lookup(obj):
    """
    Returns a list of available attributes and methods of an object.
    Args:
    - obj: object to get attributes and methods of
    Returns:
    - list: list of available attributes and methods of the object
    """
    return dir(obj)
