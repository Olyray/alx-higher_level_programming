#!/usr/bin/python3
"""A function to append text to the end of a file"""


def append_write(filename="", text=""):
    """
    This function appends a string at the end of a text file
    and returns the number of characters added.

    Parameters:
    filename (str): The file path of the file to be written.
    text (str): The string to be appended to the file.

    Returns:
    int: The number of characters added to the file.
    """
    with open(filename, 'a', encoding='utf8') as f:
        return f.write(text)
