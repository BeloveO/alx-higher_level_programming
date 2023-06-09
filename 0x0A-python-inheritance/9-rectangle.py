#!/usr/bin/python3
"""
Defines a class Rectangle that inherits from the BaseGeometry.
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Rectangle using BaseGeometry
    """
    def __init__(self, width, height):
        """
        Initializes instances
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Returns area of the rectangle"""
        return self.__height * self.__width

    def __str__(self):
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
