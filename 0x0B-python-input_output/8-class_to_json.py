#!/usr/bin/python3
"""
Defines a function that converts a class to JSON
"""


def class_to_json(obj):
    """
    Function that returns the dictionary description with simple data structure
    """
    return obj.__dict__
