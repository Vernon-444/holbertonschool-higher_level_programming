#!/usr/bin/python3
"""This module contains a function to add integers"""


def add_integers(a, b=98):
    """This method adds two integers

    Args:
        a (int): first integer to add
        b (int, optional): second integer, defaults to 98.

    Exceptions:
        TypeError: if non-integer type input for a
        TypeError: if non-integer type input for b

    Returns:
        int: The sum of a and b
    """

    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    if type(a) == float:
        a = int(a)
    if type(b) == float:
        b = int(b)

    return a + b
