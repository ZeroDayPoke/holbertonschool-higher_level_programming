#!/usr/bin/python3
"""
Write a function that reads a text file (UTF8) and prints it to stdout:

Prototype: def read_file(filename=""):
You must use the with statement
You don’t need to manage file permission or file doesn't exist exceptions.
You are not allowed to import any module
"""


def read_file(filename=""):
    """file read"""
    with open(filename, encoding="utf-8") as fred:
        print(fred.read(), end="")
