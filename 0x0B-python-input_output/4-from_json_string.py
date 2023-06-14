#!/usr/bin/python3
"""
Function to return object represented by json
"""
import json


def from_json_string(my_str):
    """
    Return object represented by json
    """
    return json.loads(my_str)
