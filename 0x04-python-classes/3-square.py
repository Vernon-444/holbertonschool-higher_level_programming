#!/usr/bin/python3

"""Define a class Square."""


class Square:
    """Represent a square."""
    def __init__(self, size=0):
        """This method initializes the square
        Size is the length of any side
        Size will be a private attribute
        Area is the area of square
        Area will be a private attribute"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return (self.__size ** 2)

    @property
    def size(self):
        """Retrieves size of self"""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of self square"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
