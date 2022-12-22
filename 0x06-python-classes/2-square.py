#!/usr/bin/python3
"""Create a class for Square and initialise the size"""


class Square:
    """The definition of the empty class Square"""

    def __init__(self, size=0):
        """Initialise the square
        Args:
            size (int): The private size of the square
        """
        self.__size = size
        check_int = isinstance(size, int)
        if check_int is not True:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
