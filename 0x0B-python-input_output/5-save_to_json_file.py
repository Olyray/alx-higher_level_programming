#!/usr/bin/python3
"""Write to a JSON file"""


import json


def save_to_json_file(my_obj, filename):
    """
    This function writes an object to a text file using a JSON representation.

    Parameters:
    my_obj (object): The object to be serialized to JSON and
    written to the file.
    filename (str): The file path of the file to be written.

    Returns:
    None
    """
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
