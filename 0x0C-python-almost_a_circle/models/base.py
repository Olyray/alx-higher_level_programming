#!/usr/bin/python3
"""A module for the creation of the Base class"""

import json


class Base:
    """
    The Base class is a simple class with a private
    class attribute __nb_objects and a class constructor.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        The class constructor for the Base class.

        Parameters:
            id (int, optional): The id for the object.
            If not provided, it will be automatically assigned.

        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns the JSON string representation of a list of dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes the JSON string representation of a list of objects to a file
        """
        filename = cls.__name__ + ".json"
        if list_objs is None:
            json_string = "[]"
        else:
            json_list = []
            for obj in list_objs:
                json_list.append(obj.to_dictionary())
            json_string = cls.to_json_string(json_list)

        with open(filename, "w") as file:
            file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """
        Returns the list represented by a JSON string
        """
        if json_string is None or json_string == "":
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Returns an instance with all attributes already set
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
        Returns a list of instances from a file
        """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as file:
                json_string = file.read()
                list_dicts = cls.from_json_string(json_string)
                list_objs = []
                for d in list_dicts:
                    list_objs.append(cls.create(**d))
                return list_objs
        except FileNotFoundError:
            return []
