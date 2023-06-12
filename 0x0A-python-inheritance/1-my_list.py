#!/usr/bin/python3
"""
Function that defines an inherited class
"""


class MyList(list):
    """
    Implements sorted printing for the built-in list class
    """
    def print_sorted(self):
        print(sorted(self))
