#!/usr/bin/python3
"""
Write a function that checks for lowercase character.

Prototype: def islower(c):
Returns True if c is lowercase
Returns False otherwise
You are not allowed to import any module
You are not allowed to use str.upper() and str.isupper()
Tips: ord()
You don’t need to understand __import__
"""
def islower(chr):
    if ord(chr) > 96 and ord(chr) < 123:
        return True
    else:
        return False
