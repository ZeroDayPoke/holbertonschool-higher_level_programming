#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tmp1 = tuple_a[0] if len(tuple_a) > 0 else 0
    tmp2 = tuple_a[1] if len(tuple_a) > 1 else 0
    tmp3 = tuple_b[0] if len(tuple_b) > 0 else 0
    tmp4 = tuple_b[1] if len(tuple_b) > 1 else 0
    return (tmp1 + tmp3, tmp2 + tmp4)
