#!/usr/bin/python3
"""unit tests for base.py"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import os


class TestBase(unittest.TestCase):
    """da UWUnit tests"""
    def test_non(self):
        base1 = Base(None)
        base2 = Base()
        self.assertEqual(base1.id + 1, base2.id)

    def test_int(self):
        self.assertEqual(Base(1).id, 1)

    def test_flt(self):
        self.assertEqual(Base(1.1).id, 1.1)

    def test_chr(self):
        self.assertEqual(Base('a').id, 'a')

    def test_str(self):
        self.assertEqual(Base("hi").id, "hi")

    def test_boo(self):
        self.assertEqual(Base(True).id, True)

    def test_lst(self):
        self.assertEqual(Base([1, 1]).id, [1, 1])

    def test_dic(self):
        self.assertEqual(Base({"richard": 1}).id, {"richard": 1})

    def test_tup(self):
        self.assertEqual(Base((1, 1)).id, (1, 1))

    def test_set(self):
        self.assertEqual(Base({1, 1}).id, {1, 1})

    def test_privacy_1(self):
        with self.assertRaises(AttributeError):
            print(Base.__nb_objects)

    def test_jason(self):
        with self.assertRaises(TypeError):
            Base.to_json_string()

    def test_counter(self):
        Square(3)
        Rectangle(3, 2)
        cnttest = Base()
        self.assertEqual(cnttest.id, 3)

    def test_jason_rekt(self):
        rekt1 = Rectangle(2, 2, 2, 2, 2)
        rekt1_dict = rekt1.to_dictionary()
        self.assertEqual(type(Base.to_json_string([rekt1_dict])), str)

    def test_jason_sqr(self):
        sqr1 = Square(2, 2, 2, 2)
        sqr1_dict = sqr1.to_dictionary()
        self.assertEqual(type(Base.to_json_string([sqr1_dict])), str)

    def test_jason_empty(self):
        dict1 = []
        js = Base.to_json_string(dict1)
        self.assertEqual(len(js), 2)

    def test_jason_none(self):
        dict1 = None
        js = Base.to_json_string(dict1)
        self.assertEqual(len(js), 2)

    @classmethod
    def dracarys(self):
        try:
            os.remove("Square.json")
        except IOError:
            pass
        try:
            os.remove("Rectangle.json")
        except IOError:
            pass
        try:
            os.remove("Base.json")
        except IOError:
            pass

    def test_stf_sqr(self):
        sqr1 = Square(1, 1, 1, 1)
        Square.save_to_file([sqr1])
        with open("Square.json") as fred:
            self.assertEqual(len(fred.read()), 38)

    def test_stf_rkt(self):
        rekt1 = Rectangle(1, 1, 1, 1, 1)
        Rectangle.save_to_file([rekt1])
        with open("Rectangle.json") as fred:
            self.assertEqual(len(fred.read()), 52)

if __name__ == '__main__':
    unittest.main()
