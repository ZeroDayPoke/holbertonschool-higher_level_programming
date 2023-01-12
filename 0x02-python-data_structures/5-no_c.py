#!/usr/bin/python3
def no_c(my_string):
    the_string = ""
    for the_char in my_string:
        if the_char != 'c' and the_char != 'C':
            the_string += the_char
    return the_string
