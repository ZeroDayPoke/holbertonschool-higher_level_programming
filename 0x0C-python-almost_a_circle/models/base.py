#!/usr/bin/python3
"""almost a circle module"""
import json
import csv


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

    @staticmethod
    def from_json_string(json_string):
        if json_string == "[]" or json_string is None:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        if dictionary:
            if cls.__name__ == "Square":
                nrich = cls(1)
            elif cls.__name__ == "Rectangle":
                nrich = cls(1, 1)
            nrich.update(**dictionary)
            return nrich

    @classmethod
    def load_from_file(cls):
        fname = cls.__name__ + ".json"
        try:
            with open(fname) as jason:
                richards = Base.from_json_string(jason.read())
                return [cls.create(**swag) for swag in richards]
        except IOError:
            return []

    @classmethod
    def load_from_file_csv(cls):
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, mode="r") as f:
                reader = csv.reader(f)
                obj_list = []
                for row in reader:
                    if cls.__name__ == "Rectangle":
                        obj_dict = {
                            "id": int(row[0]),
                            "width": int(row[1]),
                            "height": int(row[2]),
                            "x": int(row[3]),
                            "y": int(row[4])
                        }
                    elif cls.__name__ == "Square":
                        obj_dict = {
                            "id": int(row[0]),
                            "size": int(row[1]),
                            "x": int(row[2]),
                            "y": int(row[3])
                        }
                    obj_list.append(cls.create(**obj_dict))
                return obj_list
        except FileNotFoundError:
            return []
