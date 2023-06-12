#!/usr/bin/python3
"""
Function that returns list of available attributes of an object
"""


def lookup(obj):
    """
    Function to return list of available atrributes of an object
    """
    return dir(obj)
