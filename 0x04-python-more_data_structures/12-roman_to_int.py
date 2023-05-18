#!/usr/bin/python3
def roman_to_int(roman_string):
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    if (not isinstance(roman_string, str) or roman_string is None):
        return None
    res = 0
    for i in range(len(roman_string) - 1, -1, -1):
        num = roman[roman_string[i]]
        if 3 * num < res:
            res = res - num
        else:
            res = res + num
    return (res)
