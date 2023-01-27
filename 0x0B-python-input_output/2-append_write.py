#!/usr/bin/python3
"""mod com"""


def append_write(filename="", text=""):
    """file append"""
    with open(filename, 'a', encoding="utf-8") as fred:
        return fred.write(text)
