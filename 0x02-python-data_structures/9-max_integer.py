#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    int_max = my_list[0]
    for numb in my_list:
        if numb > int_max:
            int_max = numb
    return int_max
