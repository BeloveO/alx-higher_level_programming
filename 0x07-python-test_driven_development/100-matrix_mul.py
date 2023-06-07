#!/usr/bin/python3
"""
Multiplies two matrices
"""


def matrix_mul(m_a, m_b):
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    for elems in m_a:
        if not isinstance(elems, list):
            raise TypeError("m_a must be a list of lists")
    for elems in m_b:
        if not isinstance(elems, list):
            raise TypeError("m_b must be a list of lists")
    if m_a == [] or m_a ==[[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")
    for elems in m_a:
        for i in elems:
            if not type(i) in (int, float):
                raise TypeError("m_a should contain only integers or floats")
    for elems in m_b:
        for i in elems:
            if not type(i) in (int, float):
                raise TypeError("m_b should contain only integers or floats")
    length = 0
    for elems in m_a:
        if length != 0 and length != len(elems):
            raise TypeError("each row of m_a must be of the same size")
        length = len(elems)
    length = 0
    for elems in m_b:
        if length != 0 and length != len(elems):
            raise TypeError("each row of m_b must be of the same size")
        length = len(elems)
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    r1 = []
    i1 = 0
    for a in m_a:
        r2 = []
        i2 = 0
        num = 0
        while (i2 < len(m_b[0])):
            num += a[i1] * m_b[i1][i2]
            if i1 == len(m_b) - 1:
                i1 = 0
                i2 += 1
                r2.append(num)
                num = 0
            else:
                i1 += 1
        r1.append(r2)
    return r1
        