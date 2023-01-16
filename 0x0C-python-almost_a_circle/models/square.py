#!/usr/bin/python3
"""The definition of a class Square"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """
    The Square class inherits from the Rectangle
    class and adds additional functionality.
    A square is a rectangle with the same width and height.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        The class constructor for the Square class.

        Parameters:
            size (int): The size of the square.
            x (int, optional): The x-coordinate of the square.
            Default is 0.
            y (int, optional): The y-coordinate of the square.
            Default is 0.
            id (int, optional): The id of the square. If not
            provided, it will be automatically assigned.

        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        Override the __str__ method to return a string
        representation of the square
        """
        return "[Square] ({}) {}/{} - {}".format(
                self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """Getter method for the size of the square"""
        return self.width

    @size.setter
    def size(self, value):
        """Setter method for the size of the square.
        Also updates the width and height of the square.
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Update the attributes of the square
        """
        if len(args) > 0:
            self.id = args[0]
        if len(args) > 1:
            self.size = args[1]
        if len(args) > 2:
            self.x = args[2]
        if len(args) > 3:
            self.y = args[3]
        else:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def to_dictionary(self):
        """
        Returns a dictionary representation of the square
        """
        return {
                'id': self.id,
                'size': self.size,
                'x': self.x,
                'y': self.y
                }
