#!/usr/bin/python3

"""Define a Square class"""


class Square:

    """Represents the square"""

    def __init__(self, size=0, position=(0, 0)):

        """Initialize the size"""

        self.size = size
        self.position = position

    @property
    def size(self):
        """Get size property"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set size property"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Get position function"""
        return self.__position

    @position.setter
    def position(self, value):
        """Set position function"""
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int) ot not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Define the area of the square"""
        return (self.__size ** 2)

    def my_print(self):
        """Print to stdout with #"""
        if self.__size == 0:
            print("")
            return
        for y in range(0, self.__postion[1]):
            print("")
        for i in range(0, self.__size):
            for x in range(0, self.__position[0]):
                print(" ", end="")
            for j in range(0, self.__size):
                print("#", end="")
            print("")
