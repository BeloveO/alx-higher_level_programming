#!/usr/bin/python3
"""
Defines a class Square that inherits from the class Rectangle.
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Class to define square from Rectangle class
    """
    def __init__(self, size):
        """Initializes instances"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def area(self):
        """Method to return a string with the area"""
        return super().area()
