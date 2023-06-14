#!/usr/bin/python3
"""
Function that reads from a file
"""


def read_file(filename=""):
    """
    Read a file and print to stdout
    """
    with open(filename, "r", encoding="utf-8") as file:
        data = file.read()
        print(data, end='')
