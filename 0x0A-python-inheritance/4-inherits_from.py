#!/usr/bin/python3
"""
Function to check for inheritance amongst inherited classes
"""


def inherits_from(obj, a_class):
    """
    Check for isinstance
    """
    if type(obj) is a_class:
        return False
    return isinstance(obj, a_class)
