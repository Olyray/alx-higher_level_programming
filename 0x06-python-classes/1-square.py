#!/usr/bin/python3
"""Create a class for square and initialise the size"""


class Square:
    """The definition of the empty class Square"""

    def __init__(self, size):
        """Initialise the square
        Args:
            size (int): The private size of the square
        """
        self.__size = size
