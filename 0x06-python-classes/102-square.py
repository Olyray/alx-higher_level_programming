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

    def area(self):
        """Calculates the area of a square

        Returns:
            int: the area of the square calculated
        """
        square_area = self.__size * self.__size
        return square_area

    def __eq__(self, other):
        """Overloads the equals to operator

        Returns:
            int: The result of the overloaded operator
        """
        if self.area() == other.area():
            return True
        else:
            return False

    def __lt__(self, other):
        """Overloads the equals to operator

        Returns:
            int: The result of the overloaded operator
        """
        if self.area() < other.area():
            return True
        else:
            return False

    def __ne__(self, other):
        """Overloads the not equals to operator

        Returns:
            The result of the overloaded operator
        """
        return self.area() != other.area()

    def __gt__(self, other):
        """Overloads the greater than operator

        Returns:
            int: The result of the overloaded operator
        """
        return self.area() > other.area()

    def __ge__(self, other):
        """Overloads the greater than or equals to operator

        Returns:
            int: The result of the overloaded operator
        """
        return self.area() >= other.area()

    def __le__(self, other):
        """Overloads the less than or equals to operator

        Returns:
            int: The result of the overloaded operator
        """
        return self.area() <= other.area()

    @property
    def size(self):
        """str: this is the setter for self
        Args:
            value (int): this is the value that wants to be
                changed in the setter.
        Raises:
            TypeError: this is done when the value isn't an
                integer.
            ValueError: This is for when value is a negative number.
        """
        return self.__size

    @size.setter
    def size(self, value):
        check_int = isinstance(value, int)
        if check_int is not True:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
