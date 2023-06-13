#!/usr/bin/python3
"""
Function with an exception
"""


class BaseGeometry():
    """
    Class that raises an exception
    """
    def area(self):
        raise Exception("area() is not implemented")
