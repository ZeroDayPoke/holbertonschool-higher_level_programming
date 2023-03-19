#!/usr/bin/python3
"""
Write a function that returns the weighted average
of all integers tuple (<score>, <weight>)

Prototype: def weight_average(my_list=[]):
Returns 0 if the list is empty
You are not allowed to import any module
"""

def weight_average(my_list=[]):
    """return 0 if list empty"""
    if not my_list:
        return 0

    """init totals"""
    total_score = 0
    total_weight = 0

    """iterates thru tup"""
    for score, weight in my_list:
        """add to respective totals"""
        total_score += score * weight
        total_weight += weight

    """compute weighted avg"""
    weighted_average = total_score / total_weight
    return weighted_average
