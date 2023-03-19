#!/usr/bin/python3
"""
Technical interview preparation:

You are not allowed to google anything
Whiteboard first
Create a function def roman_to_int(roman_string):
that converts a Roman numeral to an integer.

You can assume the number will be between 1 to 3999.
def roman_to_int(roman_string) must return an integer
If the roman_string is not a string or None, return 0
"""


def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    rom = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    int_stor = 0
    for ii in range(len(roman_string)):
        if ii > 0 and rom[roman_string[ii]] > rom[roman_string[ii - 1]]:
            int_stor += rom[roman_string[ii]] - 2 * rom[roman_string[ii - 1]]
        else:
            int_stor += rom[roman_string[ii]]
    return int_stor
