#!/usr/bin/python3
"""doc test"""


def print_square(size):
    """doc test"""
    if not isinstance(size, int):
        if isinstance(size, float) and size < 0:
            raise TypeError("size must be an integer")
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for it_i in range(size):
        print("#" * size)
