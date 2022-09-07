#!/usr/bin/python3

"""Define a class Square."""


class Square:
    """Represent a square."""
    def __init__(self, size=0):
        """This method initializes the square
        Size is the length of any side
        Size will be a private attribute"""
        self.__size = size
