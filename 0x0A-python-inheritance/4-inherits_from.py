#!/usr/bin/python3
"""placeholder"""


def inherits_from(obj, a_class):
    """placeholder"""
    if type(obj) != a_class and issubclass(type(obj), a_class):
        return True
    return False
