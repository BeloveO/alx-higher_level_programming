#!/usr/bin/python3
"""
Function to check isinstance
"""


def is_same_class(obj, a_class):
    """
    Returns True if obj is exactly an instance of a_class
    """
    if type(obj) == a_class:
        return True
    else:
        return False
