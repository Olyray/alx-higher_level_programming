#!/usr/bin/python3
"""A function to serialise a JSON string"""


import json


def to_json_string(my_obj):
    """
    This function returns the JSON representation of an object.

    Parameters:
    my_obj (object): The object to be serialized to JSON.

    Returns:
    str: The JSON representation of the object.
    """
    return json.dumps(my_obj)
