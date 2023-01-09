#!/usr/bin/python3
"""Checks if an object is an instance of a class
that inherits from the class in question.
"""


def inherits_from(obj, a_class):
    """
    Returns True if the object is an instance of a class
    that inherited (directly or indirectly) from the specified class;
    otherwise False.

    Args:
    - obj: object to check
    - a_class: class to check against

    Returns:
    - bool: True if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class; otherwise False
    """
    return type(obj) != a_class
