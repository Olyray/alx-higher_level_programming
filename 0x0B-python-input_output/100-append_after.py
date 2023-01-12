#!/usr/bin/python3
"""A function to add a string after a specific line"""


def append_after(filename="", search_string="", new_string=""):
    """
    This function inserts a line of text to a file, after
    each line containing a specific string.

    Parameters:
    filename (str): The file path of the file to be modified.
    search_string (str): The string that the function will
    search for in the file.
    new_string (str): The string that will be inserted after
    each line containing the search_string.

    Returns:
    None
    """
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            lines.append(line)
            if search_string in line:
                lines.append(new_string)
    with open(filename, 'w') as f:
        f.writelines(lines)
