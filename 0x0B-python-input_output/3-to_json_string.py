#!/usr/bin/python3
"""
Defines a function that returns JSON representation of object
"""


import json
def to_json_string(my_obj):
    """
    Converts a object into JSON representation
    """
    json_rep = json.dumps(my_obj)
    return json_rep
