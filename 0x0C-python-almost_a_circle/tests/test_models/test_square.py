#!/usr/bin/python3
"""unit tests for square.py"""
import unittest
from models.square import Square
from models.base import Base
from models.rectangle import Rectangle
import os
from io import StringIO
import sys


class TestSquare(unittest.TestCase):
    """da UWUnit tests"""
    def test_if_base(self):
        self.assertIsInstance(Square(1), Base)

    def test_if_rekt(self):
        self.assertIsInstance(Square(1), Rectangle)

    def test_update_1(self):
        sqr1 = Square(1, 1, 1, 1)
        sqr1.update(2)
        self.assertEqual(sqr1.id, 2)

    def test_update_2(self):
        sqr1 = Square(1, 1, 1, 1)
        sqr1.update(2, 2)
        self.assertEqual(sqr1.size, 2)

    def test_update_3(self):
        sqr1 = Square(1, 1, 1, 1)
        sqr1.update(2, 2, 2)
        self.assertEqual(sqr1.x, 2)

    def test_update_4(self):
        sqr1 = Square(1, 1, 1, 1)
        sqr1.update(2, 2, 2, 2)
        self.assertEqual(sqr1.y, 2)

    def test_upd_kwa_1(self):
        sqr1 = Square(1, 1, 1, 1)
        sqr1.update(id=2)
        self.assertEqual(sqr1.id, 2)

    def test_upd_kwa_2(self):
        sqr1 = Square(1, 1, 1, 1)
        sqr1.update(size=2)
        self.assertEqual(sqr1.size, 2)

    def test_upd_kwa_3(self):
        sqr1 = Square(1, 1, 1, 1)
        sqr1.update(x=2)
        self.assertEqual(sqr1.x, 2)

    def test_upd_kwa_4(self):
        sqr1 = Square(1, 1, 1, 1)
        sqr1.update(y=2)
        self.assertEqual(sqr1.y, 2)

    def test_upd_kwa_5(self):
        sqr1 = Square(2, 2, 2, 2)
        sqr1.update(id=5, y=3)
        self.assertEqual(sqr1.id, 5)
        self.assertEqual(sqr1.y, 3)

    def test_upd_kwa_6(self):
        sqr1 = Square(2, 2, 2, 2)
        sqr1.update(size=1, x=1, y=1, id=1)
        self.assertEqual(sqr1.id, 1)

    def test_str_sqr(self):
        sqr1 = Square(1, 1, 1, 1)
        sqrstr1 = sqr1.__str__()
        sqrstr2 = '[Square] (1) 1/1 - 1'
        self.assertEqual(sqrstr1, sqrstr2)

    def test_privacy_1(self):
        with self.assertRaises(AttributeError):
            print(Square(1, 1, 1, 1).__id)

    def test_privacy_2(self):
        with self.assertRaises(AttributeError):
            print(Square(1, 1, 1, 1).__size)

    def test_privacy_3(self):
        with self.assertRaises(AttributeError):
            print(Square(1, 1, 1, 1).__x)

    def test_privacy_4(self):
        with self.assertRaises(AttributeError):
            print(Square(1, 1, 1, 1).__y)

    def test_arg_limit(self):
        with self.assertRaises(TypeError):
            Square(1, 2, 3, 4, 5)

    def test_okay_sqr(self):
        sqr1 = Square(3, 0, 0, 1)
        self.assertEqual(sqr1.area(), 9)

    def test_size_init(self):
        sqr1 = Square(3)
        self.assertEqual(sqr1.width, sqr1.size)
        self.assertEqual(sqr1.height, sqr1.size)

    def test_flt_x(self):
        with self.assertRaises(TypeError):
            Square(3, 2.2)

    def test_non_x(self):
        with self.assertRaises(TypeError):
            Square(3, None)

    def test_chr_x(self):
        with self.assertRaises(TypeError):
            Square(3, 'a')

    def test_str_x(self):
        with self.assertRaises(TypeError):
            Square(3, "UWU")

    def test_boo_x(self):
        with self.assertRaises(TypeError):
            Square(3, True)

    def test_lst_x(self):
        with self.assertRaises(TypeError):
            Square(3, [2, 2])

    def test_dic_x(self):
        with self.assertRaises(TypeError):
            Square(3, {"size": 1})

    def test_set_x(self):
        with self.assertRaises(TypeError):
            Square(3, {1, 1})

    def test_tup_x(self):
        with self.assertRaises(TypeError):
            Square(3, (1, 1))

    def test_ngv_x(self):
        with self.assertRaises(ValueError):
            Square(3, -3)

    def test_zed_x(self):
        sqr1 = Square(3, 0)
        self.assertEqual(sqr1.x, 0)

    def test_flt_y(self):
        with self.assertRaises(TypeError):
            Square(3, 3, 2.2)

    def test_non_y(self):
        with self.assertRaises(TypeError):
            Square(3, 3, None)

    def test_chr_y(self):
        with self.assertRaises(TypeError):
            Square(3, 3, 'a')

    def test_str_y(self):
        with self.assertRaises(TypeError):
            Square(3, 3, "UWU")

    def test_boo_y(self):
        with self.assertRaises(TypeError):
            Square(3, 3, True)

    def test_lst_y(self):
        with self.assertRaises(TypeError):
            Square(3, 3, [2, 2])

    def test_dic_y(self):
        with self.assertRaises(TypeError):
            Square(3, 3, {"size": 1})

    def test_set_y(self):
        with self.assertRaises(TypeError):
            Square(3, 3, {1, 1})

    def test_tup_y(self):
        with self.assertRaises(TypeError):
            Square(3, 3, (1, 1))

    def test_ngv_y(self):
        with self.assertRaises(ValueError):
            Square(3, 3, -3)

    def test_richard(self):
        sqr1 = Square(1, 1, 1 ,1)
        richard = {"id": 1, "size": 1, "x": 1, "y": 1}
        dick = sqr1.to_dictionary()
        self.assertEqual(richard, dick)

    def test_get_size(self):
        sqr1 = Square(8)
        self.assertEqual(8, sqr1.size)

    def test_get_x(self):
        sqr1 = Square(8, 6)
        self.assertEqual(6, sqr1.x)

    def test_get_y(self):
        sqr1 = Square(8, 6, 7)
        self.assertEqual(7, sqr1.y)

    def test_get_id(self):
        sqr1 = Square(8, 6, 7, 5)
        self.assertEqual(5, sqr1.id)

    def test_set_size(self):
        sqr1 = Square(8)
        sqr1.size = 1
        self.assertEqual(1, sqr1.size)

    def test_set_x(self):
        sqr1 = Square(8, 6)
        sqr1.x = 1
        self.assertEqual(1, sqr1.x)

    def test_set_y(self):
        sqr1 = Square(8, 6, 7)
        sqr1.y = 1
        self.assertEqual(1, sqr1.y)

    def test_set_id(self):
        sqr1 = Square(8, 6, 7, 5)
        sqr1.id = 1
        self.assertEqual(1, sqr1.id)

    def test_dic_bad(self):
        sqr1 = Square(8, 6, 7, 5)
        with self.assertRaises(TypeError):
            sqr1.to_dictionary(777)

    def test_str_bad(self):
        sqr1 = Square(8, 6, 7, 5)
        with self.assertRaises(TypeError):
            sqr1.__str__(777)

    def test_are_bad(self):
        sqr1 = Square(8, 6, 7, 5)
        with self.assertRaises(TypeError):
            sqr1.area(777)

    def test_dis_bad(self):
        sqr1 = Square(8, 6, 7, 5)
        with self.assertRaises(TypeError):
            sqr1.display(777)

    def test_jason_empty(self):
        dict1 = []
        js = Square.to_json_string(dict1)
        self.assertEqual(len(js), 2)

    def test_jason_none(self):
        dict1 = None
        js = Square.to_json_string(dict1)
        self.assertEqual(len(js), 2)

    def test_flt_reg(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(2.2)

    def test_non_reg(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(None)

    def test_chr_reg(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square('a')

    def test_str_reg(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("UWU")

    def test_boo_reg(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(True)

    def test_lst_reg(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square([2, 2])

    def test_dic_reg(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square({"size": 1})

    def test_set_reg(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square({1, 1})

    def test_tup_reg(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square((1, 1))

    def test_ngv_reg(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-3)

    def test_zed_reg(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(0)

    def test_flt_reg_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(2, 2.2)

    def test_non_reg_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(2, None)

    def test_chr_reg_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(2, 'a')

    def test_str_reg_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(2, "UWU")

    def test_boo_reg_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(2, True)

    def test_lst_reg_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(2, [2, 2])

    def test_dic_reg_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(2, {"size": 1})

    def test_set_reg_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(2, {1, 1})

    def test_tup_reg_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(2, (1, 1))

    def test_ngv_reg_x(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(2, -3)

    def test_flt_reg_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(2, 2, 2.2)

    def test_non_reg_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(2, 2, None)

    def test_chr_reg_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(2, 2, 'a')

    def test_str_reg_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(2, 2,"UWU")

    def test_boo_reg_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(2, 2, True)

    def test_lst_reg_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(2, 2, [2, 2])

    def test_dic_reg_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(2, 2, {"size": 1})

    def test_set_reg_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(2, 2, {1, 1})

    def test_tup_reg_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(2, 2, (1, 1))

    def test_ngv_reg_y(self):
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(2, 2, -3)

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

    def test_stf_sqr_2(self):
        sqr1 = Square(1, 1, 1, 1)
        sqr2 = Square(2, 2, 2, 2)
        Square.save_to_file([sqr1, sqr2])
        with open("Square.json") as fred:
            self.assertEqual(len(fred.read()), 76)

    def test_stf_sqr_mpt(self):
        Square.save_to_file([])
        with open("Square.json") as fred:
            self.assertEqual(len(fred.read()), 2)

    def test_stf_sqr_non(self):
        Square.save_to_file(None)
        with open("Square.json") as fred:
            self.assertEqual(len(fred.read()), 2)

    def test_fjs_sqr(self):
        sqr1 = Square(1, 1, 1, 1)
        dick1 = sqr1.to_dictionary()
        jason_in = Square.to_json_string([dick1])
        jason_out = Square.from_json_string(jason_in)
        self.assertEqual(len(str(dick1)) + 2, len(str(jason_out)))

    def test_crt_sqr(self):
        sqr1 = Square(1, 1, 1, 1)
        dick1 = sqr1.to_dictionary()
        sqr11 = Square.create(**dick1)
        self.assertEqual(str(sqr11), str(sqr1))

    def test_lff_sqr(self):
        sqr1 = Square(1, 1, 1, 1)
        sqr2 = Square(2, 2, 2, 2)
        Square.save_to_file([sqr1, sqr2])
        sqrlst = Square.load_from_file()
        self.assertEqual(str(sqr2), str(sqrlst[1]))

    @staticmethod
    def disp_yoink(shape):
        yoink = StringIO()
        sys.stdout = yoink
        shape.display()
        sys.stdout = sys.__stdout__
        return yoink

    def test_sqr_dis(self):
        sqr1 = Square(2, 1, 1, 1)
        yoink = TestSquare.disp_yoink(sqr1)
        sqrstr = "\n ##\n ##\n"
        self.assertEqual(yoink.getvalue(), sqrstr)

    def test_sqr_dis_nof(self):
        sqr1 = Square(2, 0, 0, 0)
        yoink = TestSquare.disp_yoink(sqr1)
        sqrstr = "##\n##\n"
        self.assertEqual(yoink.getvalue(), sqrstr)

    def test_str_sqr_nof(self):
        sqr1 = Square(1, 0, 0, 1)
        sqrstr1 = sqr1.__str__()
        sqrstr2 = '[Square] (1) 0/0 - 1'
        self.assertEqual(sqrstr1, sqrstr2)

if __name__ == '__main__':
    unittest.main()
