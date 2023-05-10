#!/usr/bin/python3
def fizzbuzz():
    for a in range(1, 101):
        if a % 3 and a % 5:
            print("FizzBuzz", end='')
        elif a % 3:
            print("Fizz", end='')
        elif a % 5:
            print("Buzz", end='')
        else:
            print(a, end='')
        print(" ", end='')
