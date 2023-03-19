#!/usr/bin/python3
"""
Write a function that returns the JSON representation of an object (string):

Prototype: def to_json_string(my_obj):
You don’t need to manage exceptions if the object can’t be serialized.
"""
import json


def to_json_string(my_obj):
    "to json str"
    return json.dumps(my_obj)
