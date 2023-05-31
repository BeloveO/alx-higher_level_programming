#!/usr/bin/python3
"""

Define class Square

"""


class Square:
    """Represent a square."""
    @property
    def size(self):
        """ Get/set the current size of the square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """Method to set the size value of the square object."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = int(value)

    def area(self):
        """ Method that returns the area of the square object
        """
        return (self.__size ** 2)

    def __init__(self, size=0):
        """ Method to initialize the square object
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = int(size)
