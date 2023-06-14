#!/usr/bin/python3
"""
Function that writes to a file and return number of characters
"""


def write_file(filename="", text=""):
    """
    Write to a file
    """
    num = 0
    with open(filename, "w", encoding="utf-8") as file:
        data = file.write(text)
        for a in text:
            num += 1
        return (num)
