#!/usr/bin/python3
"""
Write a function that deletes the item at a specific position in a list.

Prototype: def delete_at(my_list=[], idx=0):
If idx is negative or out of range, nothing change (returns the same list)
You are not allowed to use pop()
You are not allowed to import any module
"""
def delete_at(my_list=[], idx=0):
    if idx < len(my_list) and idx >= 0:
        del my_list[idx]
    return my_list
