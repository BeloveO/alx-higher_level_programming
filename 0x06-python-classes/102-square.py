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
        if type(value) is not int and type(value) is not float:
            raise TypeError("size must be a number")
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

    def __eq__(self, other):
        """ Define the == comparison of the Square class
        """
        return (self.__size == other.__size)

    def __lt__(self, other):
        """Define the < comparison of the Square class
        """
        return (self.__size < other.__size)

    def __le__(self, other):
        """Define the <= comparison of the Square class
        """
        return (self.__size <= other.__size)

    def __ne__(self, other):
        """Define the != comparison of the Square class
        """
        return (self.__size != other.__size)

    def __gt__(self, other):
        """Define the > comparison of the Square class
        """
        return (self.__size > other.__size)

    def __ge__(self, other):
        """Define the >= comparison of the Square class
        """
        return (self.__size >= other.__size)
