#!/usr/bin/python3
def uniq_add(my_list=[]):
    return sum(valx for valx in set(my_list) if isinstance(valx, int))
