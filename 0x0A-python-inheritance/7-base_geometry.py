#!/usr/bin/python3
"""A base geometry class."""


class BaseGeometry:
    """Class with public instance method."""

    def area(self):
        """method that raises an exception."""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates the value."""

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
