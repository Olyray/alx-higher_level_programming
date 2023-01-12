#!/usr/bin/python3
"""Module for a function to read a file"""


def read_file(filename=""):
    """
    This function reads a text file and prints its contents to stdout.

    Parameters:
    filename (str): The file path of the file to be read.

    Returns:
    None
    """
    with open(filename, 'r', encoding='utf8') as f:
        print(f.read(), end = "")
