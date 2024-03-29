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
            json_str = cls.to_json_string(
                [items.to_dictionary() for items in new_list])
            file.write(json_str)

    @staticmethod
    def from_json_string(json_string):
        json_list = []
        if json_string is None:
            return json_list
        else:
            json_list = json.loads(json_string)
            return json_list

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == "Rectangle":
            dummy_inst = cls(1, 1)
        else:
            dummy_inst = cls(1)
        dummy_inst.update(**dictionary)
        return dummy_inst

    @classmethod
    def load_from_file(cls):
        """
        Return a class instantied from a dictionary of attributes
        """
        name_of_file = cls.__name__ + ".json"
        try:
            with open(name_of_file, 'r') as file:
                json_read = file.read()
                json_dicts = Base.from_json_string(json_read)
                result_inst = []
                for dictionary in json_dicts:
                    inst = cls.create(**dictionary)
                    if inst:
                        result_inst.append(inst)
                return result_inst
        except FileNotFoundError:
            return []
