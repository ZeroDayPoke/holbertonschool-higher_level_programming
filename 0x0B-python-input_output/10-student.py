#!/usr/bin/python3
"""json mod"""


class Student:
    """study class"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if type(attrs) == list:
            if all(type(attr) == str for attr in attrs):
                return {ii: getattr(self, ii)
                        for ii in attrs if hasattr(self, ii)}
        else:
            return self.__dict__
