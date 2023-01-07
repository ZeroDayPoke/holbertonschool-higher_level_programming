#!/usr/bin/python3
def fizzbuzz():
    for numblilbug in range(1, 101):
        if numblilbug % 15 == 0:
            print("FizzBuzz ", end="")
        elif numblilbug % 3 == 0:
            print("Fizz ", end="")
        elif numblilbug % 5 == 0:
            print("Buzz ", end="")
        else:
            print("{} ".format(numblilbug), end="")
