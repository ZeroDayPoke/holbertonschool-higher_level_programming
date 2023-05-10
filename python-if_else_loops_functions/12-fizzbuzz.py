#!/usr/bin/python3
"""
Write a function that prints the numbers from 1 to 100 separated by a space.

For multiples of three print Fizz instead of the number and
for multiples of five print Buzz.
For numbers which are multiples of both three and five print FizzBuzz.
Prototype: def fizzbuzz():
Each element should be followed by a space
You are not allowed to import any module
You don’t need to understand __import__
"""


def fizzbuzz():
    """FizzBuzz"""
    for numblilbug in range(1, 101):
        if numblilbug % 15 == 0:
            print("FizzBuzz ", end="")
        elif numblilbug % 3 == 0:
            print("Fizz ", end="")
        elif numblilbug % 5 == 0:
            print("Buzz ", end="")
        else:
            print("{} ".format(numblilbug), end="")
