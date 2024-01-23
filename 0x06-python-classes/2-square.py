#!/usr/bin/python3
"""
This module defines a Square class.
"""


class Square:
    """
    This class represents a square.

    Attributes:
        __size (int): The size of the square.
    """

    def __init__(self, size=0):
        """
        Initializes a new instance of the Square class.
        """

        elif self.__size < 0:
            raise ValueError("size must be >= 0")

        if not isinstance(self.__size, int):
            raise TypeError("size must be an integer")

        self.__size = size
