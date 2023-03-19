#!/usr/bin/python3
"""
Write a function that computes the square
value of all integers of a matrix using map

Prototype: def square_matrix_map(matrix=[]):
matrix is a 2 dimensional array
Returns a new matrix:
Same size as matrix
Each value should be the square of the value of the input
Initial matrix should not be modified
You are not allowed to import any module
You have to use map
You are not allowed to use for or while
Your file should be max 3 lines
"""
def square_matrix_map(matrix=[]):
    return list(map(lambda row: list(map(lambda val: val ** 2, row)), matrix))
