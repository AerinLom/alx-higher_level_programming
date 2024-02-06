#!/usr/bin/python3
"""
Defines a function that creates an Object from a “JSON file”
"""
import json


def load_from_json_file(filename):
    """
    JSON file converted into object
    """
    with open(filename, "r") as file:
        new_obj = json.load(file)
        return new_obj
