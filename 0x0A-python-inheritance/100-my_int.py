#!/usr/bin/python3
"""
Class MyInt that inherits from int
"""


class MyInt(int):
    """
    Methods that return == and != are inverted
    """
    def __eq__(self, other):
        return int.__ne__(self, other)

    def __ne__(self, other):
        return int.__eq__(self, other)
