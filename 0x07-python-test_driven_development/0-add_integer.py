#!/usr/bin/python3
"""
Module 0-add_integer - defines a function that adds integers.
Usage: add_integer(3, 5)
result = 8
"""


def add_integer(a, b=98):
    """
    Return the sum of a and b
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return (int(a) + int(b))
