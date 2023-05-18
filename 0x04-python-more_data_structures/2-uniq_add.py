#!/usr/bin/python3
def uniq_add(my_list=[]):
    list_set = set(my_list)
    su_m = 0
    for i in list_set:
        su_m += i
    return (su_m)
