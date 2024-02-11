#!/usr/bin/python3
"""
This module defines a Base class for object creation.
"""
import json


class Base:
    """
    Base class for object creation with an id.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None:
            return ("[]")
        else:
            json_str_rep = json.dumps(list_dictionaries)
            return json_str_rep

    @classmethod
    def save_to_file(cls, list_objs):
        new_list = []
        if list_objs is None:
            return new_list
        name_of_file = cls.__name__ + ".json"
        with open(name_of_file, 'w') as file:
            new_list = list_objs
            json_str = cls.to_json_string([items.to_dictionary() for items in new_list])
            file.write(json_str)

    @staticmethod
    def from_json_string(json_string):
        json_list = []
        if json_string is None:
            return json_list
        else:
            json_list = json.loads(json_string)
            return json_list
