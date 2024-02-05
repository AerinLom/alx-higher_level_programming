#!/usr/bin/python3
"""
This module defines a lookup function.
"""


def lookup(obj):
    """
    returns list of available attributes and methods of object
    """
    return dir(obj)
