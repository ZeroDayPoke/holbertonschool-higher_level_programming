#!/usr/bin/python3
"""json mod"""
import json


def load_from_json_file(filename):
    "load from json"
    with open(filename) as fred:
        return json.load(fred)
