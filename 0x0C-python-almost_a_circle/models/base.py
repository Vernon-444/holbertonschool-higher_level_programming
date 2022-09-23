#!/usr/bin/python3
"""Is the 'Base' of all other classes in this project.
The goal of it is to manage id attribute in all future
classes & avoid duplicating the same code (and bugs)"""


class Base:
    """ Represent the base model"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new Base"""

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
