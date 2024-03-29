#!/usr/bin/python3
"""Defines a rectangle class."""
from models.base import Base


class Rectangle(Base):
    """Represent a rectangle."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new Rectangle.

        Args:
            width (int): The width of Rectangle.
            height (int): The height of Rectangle.
            x (int): The x coordinate of Rectangle.
            y (int): The y coordinate of Rectangle.
            id (int): The identity of Rectangle.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Get the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Get the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Get the x value of the rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        """
        Set the x value of the rectangle
        """
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Get the y value of the rectangle"""
        return self.__y

    @y.setter
    def y(self, value):
        """Set the x value of the rectangle"""
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Returns the are of Rectangle"""
        area = self.width * self.height
        return area

    def display(self):
        """Prints Rectangle using `#`"""
        for vert_offset in range(self.y):
            print()
        for elements in range(self.height):
            print(" " * self.x + "#" * self.width)

    def update(self, *args, **kwargs):
        """Update the attributes of the rectangle"""
        if args:
            num_args = len(args)
            if num_args >= 1:
                self.id = args[0]
            if num_args >= 2:
                self.width = args[1]
            if num_args >= 3:
                self.height = args[2]
            if num_args >= 4:
                self.x = args[3]
            if num_args >= 5:
                self.y = args[4]
        else:
            for attribute, value in kwargs.items():
                if hasattr(self, attribute):
                    setattr(self, attribute, value)

    def to_dictionary(self):
        """Returns dictionary representation of Rectangle"""
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }

    def __str__(self):
        """Returns the string representation of Rectangle"""
        return("[Rectangle] ({}) {}/{} - {}/{}"
               .format(self.id, self.x, self.y, self.width, self.height))
