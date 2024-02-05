#!/usr/bin/python3
"""
Defines a class Rectangle and a class Square
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Represents a square, inheriting from Rectangle.
    """

    def __init__(self, size):
        """
        Initializes a Square instance with the given size.
        """
        super().__init__(size, size)
        self.__size = 0
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """
        Computes the area of the square.
        """
        return self.__size ** 2

    def __str__(self):
        """
        Returns a string representation of the square.
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
