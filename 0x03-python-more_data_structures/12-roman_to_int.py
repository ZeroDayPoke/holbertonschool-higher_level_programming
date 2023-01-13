#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    ivxlcdm = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    int_stor = 0
    for inti in range(len(roman_string)):
        if inti > 0 and ivxlcdm[roman_string[inti]] > ivxlcdm[roman_string[inti - 1]]:
            int_stor += ivxlcdm[roman_string[inti]] - 2 * ivxlcdm[roman_string[inti - 1]]
        else:
            int_stor += ivxlcdm[roman_string[inti]]
    return int_stor
