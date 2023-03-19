#!/usr/bin/python3
"""
Write a function that prints a matrix of integers.

Prototype: def print_matrix_integer(matrix=[[]]):
Format: see example
You are not allowed to import any module
You can assume that the list only contains integers
You are not allowed to cast integers into strings
You have to use str.format() to print integers
"""
def print_matrix_integer(matrix=[[]]):
    for iteri in range(len(matrix)):
        for iterj in range(len(matrix[iteri])):
            print("{:d}".format(matrix[iteri][iterj]), end="")
            if iterj != len(matrix[iteri]) - 1:
                print(" ", end="")
        print()
