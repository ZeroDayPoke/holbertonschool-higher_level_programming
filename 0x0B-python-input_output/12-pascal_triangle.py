#!/usr/bin/python3
"""triangle mod"""


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
