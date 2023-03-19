#!/usr/bin/python3
"""
Write a function that finds all multiples of 2 in a list.

Prototype: def divisible_by_2(my_list=[]):
Return a new list with True or False, depending on whether the integer at the same
position in the original list is a multiple of 2
The new list should have the same size as the original list
You are not allowed to import any module
"""
def divisible_by_2(my_list=[]):
    return [i % 2 == 0 for i in my_list]
