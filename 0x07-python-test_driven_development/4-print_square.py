#!/usr/bin/python3
"""A functoion that prints a square with #"""

def print_square(size):
    """
    Prints a square made of the character # to the console.
    
    Args:
    size (int): The size of the square, which is the length of each side.
    
    Raises:
    TypeError: If size is not an integer.
    ValueError: If size is less than 0.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("#" * size)
