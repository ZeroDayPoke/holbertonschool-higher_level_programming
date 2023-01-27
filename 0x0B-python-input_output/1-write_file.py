#!/usr/bin/python3
"""mod com"""


def write_file(filename="", text=""):
    """file write"""
    with open(filename, 'w', encoding="utf-8") as fred:
        fred.write(text)
    return len(text)
