#!/usr/bin/python3
"""
Defines a checker for a inherited class instance
"""


def inherits_from(obj, a_class):
    """
    Check if object is an instance of a class that inherited from the class
    """
    if isinstance(obj, type) and issubclass(type(obj), a_class):
        return True
    return False
