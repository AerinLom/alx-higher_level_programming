#!/usr/bin/python3
"""
This module defines a object validity checker
"""

def is_same_class(obj, a_class):
    """
    Checks for an instance of a_class
    """
    if type(obj) is a_class:
        return True
    return False
