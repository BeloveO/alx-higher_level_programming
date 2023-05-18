#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new = dict()
    for key, value in a_dictionary.items():
        val = value * 2
        new[key] = val
    return (new)
