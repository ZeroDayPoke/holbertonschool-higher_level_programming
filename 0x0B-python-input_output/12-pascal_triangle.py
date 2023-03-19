#!/usr/bin/python3
"""
Technical interview preparation:

You are not allowed to google anything
Whiteboard first
Create a function def pascal_triangle(n): that returns a list of lists of
integers representing the Pascal’s triangle of n:

Returns an empty list if n <= 0
You can assume n will be always an integer
You are not allowed to import any module
"""


def pascal_triangle(n):
    """triangle time"""
    if n <= 0:
        return []
    trian = [[1]]
    for ii in range(1, n):
        rw = [1]
        for ij in range(1, ii):
            rw.append(trian[ii-1][ij-1] + trian[ii-1][ij])
        rw.append(1)
        trian.append(rw)
    return trian
