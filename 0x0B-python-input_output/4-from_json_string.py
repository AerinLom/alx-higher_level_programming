#!/usr/bin/python3
"""
Defines a function that returns an object from JSON string
"""
import json


def from_json_string(my_str):
    """
    Returns JSON representation of python string object
    """
    py_obj = json.loads(my_str)
    return py_obj
