#!/usr/bin/python3
"""Class for Rectangle"""
from models.base import Base


class Rectangle(Base):
    """Represent a Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Containes specs of the rectangle"""

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)
