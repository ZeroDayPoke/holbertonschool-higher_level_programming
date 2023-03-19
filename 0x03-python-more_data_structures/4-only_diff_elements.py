#!/usr/bin/python3
"""
Write a function that returns a set of all elements present in only one set.

Prototype: def only_diff_elements(set_1, set_2):
You are not allowed to import any module
"""
def only_diff_elements(set_1, set_2):
    diff_eles = set()
    for ele in set_1:
        if ele not in set_2:
            diff_eles.add(ele)
    for ele in set_2:
        if ele not in set_1:
            diff_eles.add(ele)
    return diff_eles
