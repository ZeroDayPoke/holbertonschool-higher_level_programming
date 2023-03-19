#!/usr/bin/python3
"""
Write a function that replaces or adds key/value in a dictionary.

Prototype: def update_dictionary(a_dictionary, key, value):
key argument will be always a string
value argument will be any type
If a key exists in the dictionary, the value will be replaced
If a key doesn’t exist in the dictionary, it will be created
You are not allowed to import any module
"""
def update_dictionary(a_dictionary, key, value):
    a_dictionary[key] = value
    return a_dictionary
