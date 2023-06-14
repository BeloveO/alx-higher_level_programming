#!/usr/bin/python3
"""
Make a function that creates an object from json file
"""
import json


def load_from_json_file(filename):
    """
    Create object from JSON file
    """
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)
