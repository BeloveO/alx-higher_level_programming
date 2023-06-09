#!/usr/bin/python3
"""

Define class Square

"""


class Square:
    """Represent a square."""
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
