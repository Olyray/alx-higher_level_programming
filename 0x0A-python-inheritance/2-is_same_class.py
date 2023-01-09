#!/usr/bin/python3
"""A module to check if an object is an instance
   of a class.
"""


def is_same_class(obj, a_class):
    """
    Returns True if the object is exactly an instance
    of the specified class; otherwise False.

    Args:
    - obj: object to check
    - a_class: class to check against

    Returns:
    - bool: True if the object is exactly an i
    nstance of the specified class; otherwise False
    """
    return isinstance(obj, a_class)
