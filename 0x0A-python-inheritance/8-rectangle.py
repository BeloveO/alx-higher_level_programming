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
