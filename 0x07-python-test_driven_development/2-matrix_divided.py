#!/usr/bin/python3
"""
Divides all the elements of a matrix
"""


def matrix_divided(matrix, div):
    msg = "matrix must be a matrix (list of lists) of integers/floats"
    msg2 = "Each row of the matrix must have the same size"
    len_e = 0
    if (not isinstance(matrix, list) or matrix == []):
        raise TypeError(msg)
    for elem in matrix:
        if not isinstance(elem, list) or elem == []:
            raise TypeError(msg)
        if len_e != 0 and len(elem) != len_e:
            raise TypeError(msg2)
        for num in elem:
            if not type(num) in (int, float):
                raise TypeError(msg)
        len_e = len(elem)
    if not type(div) in (int, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    ans = list(map(lambda x: list(map(
        lambda y: round(y / div, 2), x)), matrix))
    return (ans)
