#!/usr/bin/python3
"""
Defines a square of a set size
"""


def print_square(size):

    """
    This function prints a square using #

    Parameters:
        size (int): The size of each side of the square
    Raises:
        TypeError: If size is not an integer and < 0
        ValueError: If size is < 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for character in range(size):
        print("#" * size)
