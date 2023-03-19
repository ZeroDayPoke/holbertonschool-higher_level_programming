#!/usr/bin/python3
"""
Write a function that returns a list with all values multiplied by a number without using any loops.

Prototype: def multiply_list_map(my_list=[], number=0):
Returns a new list:
Same length as my_list
Each value should be multiplied by number
Initial list should not be modified
You are not allowed to import any module
You have to use map
Your file should be max 3 lines
"""
def multiply_list_map(my_list=[], number=0):
    return list(map(lambda valx: valx*number, my_list))
