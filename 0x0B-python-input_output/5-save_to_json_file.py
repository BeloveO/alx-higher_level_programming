#!/usr/bin/python3
"""
Function to write object to textfile using json rep
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Write object to textfile represented by json
    """
    with open(filename, "w", encoding="utf-8") as f:
        return json.dump(my_obj, f)
