#!/usr/bin/python3
"""
Write a function that returns an object (Python data structure) represented by a JSON string:

Prototype: def from_json_string(my_str):
You don’t need to manage exceptions if the JSON string doesn’t represent an object.
"""
import json


def from_json_string(my_obj):
    "from json"
    return json.loads(my_obj)
