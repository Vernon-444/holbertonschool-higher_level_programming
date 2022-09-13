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

    def area(self):
        """Retrieves area of self rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Retrieves perimeter of self rectangle"""
        if self.__height == 0 or self.__width == 0:
            return 0
        return ((self.__height + self.__width) * 2)

    def __str__(self):
        """Returns string representation of rectangle
        that is human readable."""

        if self.__height == 0 or self.__width == 0:
            return ("")
        printable = ""
        for i in range(0, self.__height):
            printable += ("#" * self.__width)
            if i < self.__height - 1:
                printable += "\n"
        return printable

    def __repr__(self):
        """ Returns a string representation of the rectangle
        that is machine readable."""
        return("Rectangle({}, {})".format(self.__width, self.__height))
