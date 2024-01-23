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

        self.__size = size

    @property
    def size(self):
        """
        Getter used to obtain the size of the  square
        """

        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter used to set the size of the square
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value


    def area(self):

        """
        Returns the area of the current square.
        """
        return self.__size ** 2
