#!/usr/bin/python3
"""
Function that inserts a line of text after some special characters
"""


def append_after(filename="", search_string="", new_string=""):
    """
    function that inserts a line of text to a file,
    after each line containing a specific string
    """
    res = []
    with open(filename, 'r', encoding="utf-8") as file:
        for line in file:
            res += [line]
            if line.find(search_string) != -1:
                res += [new_string]
    with open(filename, 'w', encoding="utf-8") as file:
        file.write("".join(res))
