#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    a = 0
    c = 0
    for i in my_list:
        b = i[0] * i[1]
        a += b
        c += i[1]
    return (a / c)
