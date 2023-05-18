#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new = [a for a in my_list]
    for i in new:
        if i == search:
            new[new.index(i)] = replace
    return (new)
