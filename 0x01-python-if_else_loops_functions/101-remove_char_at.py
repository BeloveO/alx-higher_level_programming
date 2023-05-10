#!/usr/bin/python3
def remove_char_at(str, n):
    new_str = ""
    for a in range(len(str)):
        if a != n:
            new_str += str[a]
        return (new_str)
