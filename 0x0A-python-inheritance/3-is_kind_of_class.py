#!/usr/bin/python3
"""Checks if an object is an instance of
a class or its parent
"""


def is_kind_of_class(obj, a_class):
    """
    Returns True if the object is an instance of,
        or if the object is an instance of a class that
        inherited from, the specified class; otherwise False.

    Args:
    - obj: object to check
    - a_class: class to check against

    Returns:
    - bool: True if the object is an instance of,
        or if the object is an instance of a class that
        inherited from, the specified class; otherwise False
    """
    return isinstance(obj, a_class)
