#!/usr/bin/python3
"""mod com"""


def read_file(filename=""):
    """file read"""
    with open(filename, encoding="utf-8") as fred:
        print(fred.read(), end="")
