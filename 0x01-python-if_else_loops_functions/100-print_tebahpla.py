#!/usr/bin/python3
for a in range(90, 64, -1):
    if a % 2 == 0:
        print(chr(a + 32), end='')
    else:
        print(chr(a), end='')
