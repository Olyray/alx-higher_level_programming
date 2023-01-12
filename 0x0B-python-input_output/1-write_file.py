#!/usr/bin/python3
"""A module to write to a file"""


def write_file(filename="", text=""):
    """
    This function writes a string to a text file and
    returns the number of characters written.

    Parameters:
    filename (str): The file path of the file to be written.
    text (str): The string to be written to the file.

    Returns:
    int: The number of characters written to the file.
    """
    with open(filename, 'w', encoding='utf8') as f:
        return f.write(text)
