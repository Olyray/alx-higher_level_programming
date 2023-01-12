#!/usr/bin/python3
"""A function to serialise a JSON string"""


import json


def from_json_string(my_str):
    """
    This function returns a python object

    Parameters:
    my_str (object): The JSON to be eserialized to object.

    Returns:
    str: The python object.
    """
    return json.loads(my_str)
