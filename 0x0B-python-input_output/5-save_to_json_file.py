#!/usr/bin/python3
"""json mod"""
import json


def save_to_json_file(my_obj, filename):
    "save json"
    with open(filename, 'w') as fred:
        json.dump(my_obj, fred)
