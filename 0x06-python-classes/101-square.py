#!/usr/bin/python3
"""

Define class Square

"""


class Square:
    """Represent a square."""
    def __str__(self):
        """ Define the print representation of the square
        """
        if self.__size != 0:
            [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end='') for j in range(0, self.__position[0])]
            [print(" ", end='') for k in range(0, self.__size)]
            if i != self.__size - 1:
                print("")
        return ("")

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

    @property
    def position(self):
        """ Method that returns the position value
        """
        return (self.__position)

    @position.setter
    def position(self, value):
        """ Method that sets the position value of a square object
        """
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """ Method that returns the area of the square object
        """
        return (self.__size ** 2)

    def my_print(self):
        """ Method that prints a # square according to the size value
        """
        if self.size == 0:
            print()
        else:
            for i in range(self.position[1]):
                print()
            for i in range(self.size):
                for k in range(self.position[0]):
                    print(" ", end='')
                for j in range(self.size):
                    print("#", end='')
                print()

    def __init__(self, size=0, position=(0, 0)):
        """ Method to initialize the square object
        """
        self.size = size
        self.position = position
