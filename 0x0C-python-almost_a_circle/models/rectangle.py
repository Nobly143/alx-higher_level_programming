#!/usr/bin/python3
"""A model of a rectangle class"""

from models.base import Base


class Rectangle(Base):
    """Initialise the parts of the rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize each part of thr rectangle"""

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

        @property
        def width(self):
            """Retrieves the width attribute."""
            return self.__width

        @width.setter
        def width(self, value):
            """Set the width value"""
            if type(value) is not int:
                raise TypeError("width must be an integer")
            if value <= 0:
                raise ValueError("width must be > 0")
            self.__width = value

        @property
        def height(self):
            """Retrieve the height attribute"""
            return self.__height

        @height.setter
        def height(self, value):
            """Set the height value"""
            if type(value) is not int:
                raise TypeError("height must be an integer")
            if value <= 0:
                raise ValueError("height must be > 0")
            self.__height = value

        @property
        def x(self):
            """Retrieve the x attribute"""
            return self.__x

        @x.setter
        def x(self, value):
            """set the x value"""
            if type(value) is not int:
                raise TypeError("x must be an integer")
            if value <= 0:
                raise ValueError("x must be > 0")
            self.__x = value

        @property
        def y(self):
            """Retrieve the y attribute"""
            return self.__y

        @y.setter
        def y(self, value):
            """set the y value"""
            if type(value) is not int:
                raise TypeError("y must be an integer")
            if value <= 0:
                raise ValueError("y must be > 0")
            self.__y = value
