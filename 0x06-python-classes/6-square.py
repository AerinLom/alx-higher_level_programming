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
    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a new instance of the Square class.
        """
        self.__size = size
        self.position = position

    @property
    def size(self):
        """
        Getter used to obtain the size of the square
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

    @property
    def position(self):
        """
        Getter used to retrieve the position of the square
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter used to set the position of the square
        """
        if not (isinstance(value, tuple) and len(value) == 2
                and all(isinstance(po_val, int)
                        and po_val >= 0 for po_val in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """
        Returns the area of the current square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square with #
        """
        if self.__size == 0:
            print()
        else:
            for position_val in range(self.__position[1]):
                print()
            for size_val in range(self.__size):
                print(" " * self.__position[0] + self.__size * "#")
