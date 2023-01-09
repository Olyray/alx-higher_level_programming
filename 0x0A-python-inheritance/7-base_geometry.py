#!/usr/bin/python3
"""Add a method that validates an integer"""


class BaseGeometry:
    """
    A class representing the base geometry for other classes to inherit from.
    """

    def area(self):
        """
        Raises an exception with the message "area() is not implemented".
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that a value is a positive integer.

        Args:
        - name: string name of the value being validated
        - value: value to validate

        Raises:
        - TypeError: if value is not an integer
        - ValueError: if value is less than or equal to 0
        """
        if not type(value) == int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
