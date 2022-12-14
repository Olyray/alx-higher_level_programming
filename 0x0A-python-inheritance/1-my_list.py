#!/usr/bin/python3
"""A class that inherits from list"""


class MyList(list):
    """
    A class that inherits from list and adds a
    method to print the list in sorted order.
    """

    def print_sorted(self):
        """
        Prints the list, sorted in ascending order.
        """
        print(sorted(self))
