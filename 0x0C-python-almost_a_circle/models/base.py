#!/usr/bin/python3
"""Initiate a class"""


class Base:
    """define a private class attribute"""

    __nb_objects = 0

    def __init__(self, id=None):
        """initialize the class method"""

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
