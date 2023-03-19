#!/usr/bin/python3
"""
Write a function that writes a string to a text file (UTF8) and returns the number of characters written:

Prototype: def write_file(filename="", text=""):
You must use the with statement
You don’t need to manage file permission exceptions.
Your function should create the file if doesn’t exist.
Your function should overwrite the content of the file if it already exists.
You are not allowed to import any module
"""


def write_file(filename="", text=""):
    """file write"""
    with open(filename, 'w', encoding="utf-8") as fred:
        fred.write(text)
    return len(text)
