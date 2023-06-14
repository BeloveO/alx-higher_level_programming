#!/usr/bin/python3
"""
function that returns the dictionary description with
simple data structure (list, dictionary, string, integer
and boolean) for JSON serialization of an object
"""


def class_to_json(obj):
    """
    Function to return dict description of an obj
    """
    result = {}
    if hasattr(obj, "__dict__"):
        result = obj.__dict__.copy()
    return result
