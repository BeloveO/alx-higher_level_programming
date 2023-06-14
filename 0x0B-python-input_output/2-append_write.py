#!/usr/bin/python3
"""
Function that appends to a file and return number of characters added
"""


def append_write(filename="", text=""):
    """
    Append to a file
    """
    num = 0
    with open(filename, "a", encoding="utf-8") as file:
        data = file.write(text)
        for a in text:
            num += 1
        return (num)
