#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    a = len(sys.argv) - 1

    if a == 0:
        print("{} arguments.".format(a))
    elif a == 1:
        print("{} argument:".format(a))
    else:
        print("{} arguments:".format(a))

    for i in range(a):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
