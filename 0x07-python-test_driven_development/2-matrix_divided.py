#!/usr/bin/python3
"""doc check maybe"""


def matrix_divided(matrix, div):
    """comment test"""
    if not isinstance(matrix, list) or not all(
         isinstance(it_i, list) for it_i in matrix):
        raise TypeError("matrix must be a matrix (list of lists)"
                        " of integers/floats")
    if not all(isinstance
               (it_i, (int, float)) for lol in matrix for it_i in lol):
        raise TypeError("matrix must be a matrix (list of lists)"
                        " of integers/floats")
    if not all(len(matrix[0]) == len(lol) for lol in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(it_i / div, 2) for it_i in lol] for lol in matrix]
