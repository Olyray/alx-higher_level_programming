#!/usr/bin/python3
"""A module to print space after some symbols"""


def text_indentation(text):
    """
    Prints a string with a new line after each occurrence of ".", "?", or ":".
        If a space follows these characters, it is omitted in the output.

    Args:
    text (str): The text to be printed.

    Raises:
    TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    current_indent = 0
    icon_check = 0
    for char in text:
        if char in [".", "?", ":"]:
            print(char)
            print()
            icon_check = 1
        elif icon_check == 1:
            icon_check = 0
            continue
        else:
            print(char, end="")
