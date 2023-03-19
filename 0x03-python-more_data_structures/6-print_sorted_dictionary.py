#!/usr/bin/python3
"""
Write a function that prints a dictionary by ordered keys.

Prototype: def print_sorted_dictionary(a_dictionary):
You can assume that all keys are strings
Keys should be sorted by alphabetic order
Only sort keys of the first level (don’t sort keys of a dictionary inside the main dictionary)
Dictionary values can have any type
You are not allowed to import any module
"""
def print_sorted_dictionary(a_dictionary):
    for key, value in sorted(a_dictionary.items()):
        print("{}: {}".format(key, value))
