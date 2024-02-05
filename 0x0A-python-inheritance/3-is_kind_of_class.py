#!/usr/bin/python3
"""
This module defines an object is an instance of a class checker
"""

def is_kind_of_class(obj, a_class):
    """
    This checks if object is an instance of a class
    """
    if isinstance(obj, a_class):
        return True
    return False
