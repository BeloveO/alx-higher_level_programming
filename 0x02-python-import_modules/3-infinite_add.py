#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    sol = 0
    for arg in sys.argv:
        if arg != sys.argv[0]:
            sol += int(arg)
    print(sol)
