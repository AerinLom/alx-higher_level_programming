#!/usr/bin/python3
"""
Defines a function that writes an Object to a text file in JSON representation
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Serialize object to JSON format and write to text file
    """
    with open(filename, "w") as file:
        json.dump(my_obj, file)
