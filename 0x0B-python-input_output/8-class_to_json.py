#!/usr/bin/python3
"""json mod"""


def class_to_json(obj):
    """classy"""
    make_richard = {}
    for ky, vl in obj.__dict__.items():
        if isinstance(vl, (int, bool, str, list, dict)):
            make_richard[ky] = vl
    return make_richard
