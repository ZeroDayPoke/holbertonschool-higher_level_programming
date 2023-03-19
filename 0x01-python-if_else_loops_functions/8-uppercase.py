#!/usr/bin/python3
"""
Write a function that prints a string in uppercase followed by a new line.

Prototype: def uppercase(str):
You can only use no more than 2 print functions with string format
You can only use one loop in your code
You are not allowed to import any module
You are not allowed to use str.upper() and str.isupper()
Tips: ord()
You don’t need to understand __import__
"""
def uppercase(str):
    for char in str:
        if ord(char) > 96 and ord(char) < 123:
            char = chr(ord(char) - 32)
        print("{}".format(char), end="")
    print("")
