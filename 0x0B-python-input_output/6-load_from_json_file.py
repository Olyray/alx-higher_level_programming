#!/usr/bin/python3
"""A function to create an object from a JSON file"""


import json


def load_from_json_file(filename):
    """
    This function creates an object from a JSON file.

    Parameters:
    filename (str): The file path of the JSON file.

    Returns:
    object: The object created from the JSON file.
    """
    with open(filename, 'r') as f:
        return json.load(f)
