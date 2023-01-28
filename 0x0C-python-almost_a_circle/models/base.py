#!/usr/bin/python3
"""almost a circle module"""
import json


class Base:
    """base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        with open((cls.__name__ + ".json"), 'w') as jasonfile:
            if list_objs is None:
                jasonfile.write("[]")
            else:
                richards = [ii.to_dictionary() for ii in list_objs]
                jasonfile.write(Base.to_json_string(richards))
