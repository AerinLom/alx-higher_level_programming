#!/usr/bin/python3
"""
Defines a class Rectangle
"""


class Rectangle(BaseGeometry):
    """
    Represents a rectangle, inheriting from BaseGeometry.
    """

    def __init__(self, width, height):
        """
        Initializes a Rectangle instance with given width and height.
        """
        super().__init__()
        self.__width = 0
        self.__height = 0
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
