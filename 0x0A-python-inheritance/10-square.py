#!/usr/bin/python3
"""Implementation of a square class"""


Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    def __init__(self, size):
        """
        Initializes a Square with the given size.

        Args:
        - size: positive integer size of the square

        Raises:
        - TypeError: if size is not an integer
        - ValueError: if size is less than or equal to 0
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
