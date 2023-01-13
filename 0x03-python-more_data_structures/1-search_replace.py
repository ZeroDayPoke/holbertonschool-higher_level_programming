#!/usr/bin/python3
def search_replace(my_list, search, replace):
    return list(map(lambda varx: replace if varx == search else varx, my_list))
