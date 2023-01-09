#!/usr/bin/python3
"""An area method that raises and exception"""


class BaseGeometry:
    """
    A class representing the base geometry for other classes to inherit from.
    """

    def area(self):
        """
        Raises an exception with the message "area() is not implemented".
        """
        raise Exception("area() is not implemented")
