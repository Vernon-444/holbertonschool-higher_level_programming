#!/usr/bin/python3

"""Define a class Rectangle."""


class Rectangle:
    """Represent a Rectangle."""
    def __init__(self, width=0, height=0):
        """This method initializes the rectangle
        Width is the length of horizontal sides
        Width will be a private attribute
        Height is the length of vertical sides
        Height will be a private attribute
        Area is the area of rectangle
        Area will be a private attribute"""

        """Checking type and validity of height"""
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

        """Checking type and validity of width"""
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

    def area(self):
        return (self.__width * self.__height)

    @property
    def width(self):
        """Retrieves width of self"""
        return self.__width

    @property
    def height(self):
        """Retrieves height of self"""
        return self.__height

    @width.setter
    def width(self, value):
        """Sets the width of self rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """Sets the height of self rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
