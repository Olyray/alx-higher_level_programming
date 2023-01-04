#!/usr/bin/python3
"""This module adds two integers"""

def add_integer(a, b=98):
    """
    Adds two integers together.
    Parameters:
        a (int or float): The first integer to add.
        b (int or float, optional): The second integer to add. Defaults to 98.
    Returns:
        int: The sum of the two integers.
    Raises:
        TypeError: If `a` or `b` are not integers or floats.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return a + b
