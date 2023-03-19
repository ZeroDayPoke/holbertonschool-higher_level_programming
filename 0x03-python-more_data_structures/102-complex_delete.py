#!/usr/bin/python3
"""
Write a function that deletes keys with a
specific value in a dictionary.

Prototype: def complex_delete(a_dictionary, value):
If the value doesn’t exist, the dictionary won’t change
All keys having the searched value have to be deleted
You are not allowed to import any module
"""
def complex_delete(a_dictionary, value):
    killkeys = [key for key, val in a_dictionary.items() if val == value]
    for key in killkeys:
        del a_dictionary[key]
    return a_dictionary
