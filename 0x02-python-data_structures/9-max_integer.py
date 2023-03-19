#!/usr/bin/python3
"""
Write a function that finds the biggest integer of a list.

Prototype: def max_integer(my_list=[]):
If the list is empty, return None
You can assume that the list only contains integers
You are not allowed to import any module
You are not allowed to use the builtin max()
"""
def max_integer(my_list=[]):
    if not my_list:
        return None
    int_max = my_list[0]
    for numb in my_list:
        if numb > int_max:
            int_max = numb
    return int_max
