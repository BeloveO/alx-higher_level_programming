#!/usr/bin/python3
def uppercase(str):
    for a in range(len(str)):
        if ord(str[a]) >= 97 and ord(str[a]) <= 122:
            i = 32
        else:
            i = 0
        print("{:c}".format(ord(str[i]) - i), end='')
    print("")
