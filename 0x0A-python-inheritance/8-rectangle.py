#!/usr/bin/python3
"""Add the instantiation of width and height"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    A class to create a Rectangle
    """

    def __init__(self, width, height):
        """
        Initializes a Rectangle with the given width and height.

        Args:
        - width: positive integer width of the rectangle
        - height: positive integer height of the rectangle

        Raises:
        - TypeError: if width or height is not an integer
        - ValueError: if width or height is less than or equal to 0
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height
