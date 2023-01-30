#!/usr/bin/python3
"""unit tests for rectangle.py"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
import os


class TestRect(unittest.TestCase):
    """da UWUnit tests"""

    def test_rekt_base(self):
        self.assertIsInstance(Rectangle(2, 2), Base)

    def test_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle()

    def test_no_height(self):
        with self.assertRaises(TypeError):
            Rectangle(4)

    def test_min_args(self):
        rekt1 = Rectangle(2, 2)
        self.assertEqual(rekt1.area(), 4)

    def test_multi_rect(self):
        rekt1 = Rectangle(1, 1)
        rekt2 = Rectangle(1, 1)
        self.assertEqual(rekt1.id, rekt2.id - 1)

    def test_arg_limit(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 1, 1, 2, 2, 2)

    def test_privacy_1(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(1, 1, 1, 1, 1).__width)

    def test_privacy_2(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(1, 1, 1, 1, 1).__height)

    def test_privacy_3(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(1, 1, 1, 1, 1).__x)

    def test_privacy_4(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(1, 1, 1, 1, 1).__y)

    def test_privacy_5(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(1, 1, 1, 1, 1).__id)

    def test_flt(self):
        with self.assertRaises(TypeError):
            Rectangle(2.2, 1)

    def test_non(self):
        with self.assertRaises(TypeError):
            Rectangle(None, 1)

    def test_chr(self):
        with self.assertRaises(TypeError):
            Rectangle('a', 1)

    def test_str(self):
        with self.assertRaises(TypeError):
            Rectangle("yolo", 1)

    def test_boo(self):
        with self.assertRaises(TypeError):
            Rectangle(True, 1)

    def test_lst(self):
        with self.assertRaises(TypeError):
            Rectangle([1, 1], 1)

    def test_dic(self):
        with self.assertRaises(TypeError):
            Rectangle({"width": 1}, 1)

    def test_set(self):
        with self.assertRaises(TypeError):
            Rectangle({1, 1}, 1)

    def test_tup(self):
        with self.assertRaises(TypeError):
            Rectangle((1, 1), 1)

    def test_ngv(self):
        with self.assertRaises(ValueError):
            Rectangle(-3, 1)

    def test_zed(self):
        with self.assertRaises(ValueError):
            Rectangle(0, 1)

    def test_richard(self):
        rekt1 = Rectangle(1, 1, 1, 1 ,1)
        richard = {"id": 1, "width": 1, "height": 1, "x": 1, "y": 1}
        dick = rekt1.to_dictionary()
        self.assertEqual(richard, dick)

    def test_update_1(self):
        rekt1 = Rectangle(1, 1, 1, 1, 1)
        rekt1.update(2)
        self.assertEqual(rekt1.id, 2)

    def test_update_2(self):
        rekt1 = Rectangle(1, 1, 1, 1, 1)
        rekt1.update(2, 2)
        self.assertEqual(rekt1.width, 2)

    def test_update_3(self):
        rekt1 = Rectangle(1, 1, 1, 1, 1)
        rekt1.update(2, 2, 2)
        self.assertEqual(rekt1.height, 2)

    def test_update_4(self):
        rekt1 = Rectangle(1, 1, 1, 1, 1)
        rekt1.update(2, 2, 2, 2)
        self.assertEqual(rekt1.x, 2)

    def test_update_5(self):
        rekt1 = Rectangle(1, 1, 1, 1, 1)
        rekt1.update(2, 2, 2, 2, 2)
        self.assertEqual(rekt1.y, 2)

    def test_upd_kwa_1(self):
        rekt1 = Rectangle(1, 1, 1, 1, 1)
        rekt1.update(id=2)
        self.assertEqual(rekt1.id, 2)

    def test_upd_kwa_2(self):
        rekt1 = Rectangle(1, 1, 1, 1, 1)
        rekt1.update(width=2)
        self.assertEqual(rekt1.width, 2)

    def test_upd_kwa_3(self):
        rekt1 = Rectangle(1, 1, 1, 1, 1)
        rekt1.update(height=2)
        self.assertEqual(rekt1.height, 2)

    def test_upd_kwa_4(self):
        rekt1 = Rectangle(1, 1, 1, 1, 1)
        rekt1.update(x=2)
        self.assertEqual(rekt1.x, 2)

    def test_upd_kwa_5(self):
        rekt1 = Rectangle(1, 1, 1, 1, 1)
        rekt1.update(y=2)
        self.assertEqual(rekt1.y, 2)

    def test_upd_kwa_6(self):
        rekt1 = Rectangle(1, 1, 1, 1, 1)
        rekt1.update(x=2, y=3)
        self.assertEqual(rekt1.y, 3)
        self.assertEqual(rekt1.x, 2)

    def test_str_rekt(self):
        rekt1 = Rectangle(1, 1, 1, 1, 1)
        rektstr1 = rekt1.__str__()
        rektstr2 = '[Rectangle] (1) 1/1 - 1/1'
        self.assertEqual(rektstr1, rektstr2)

    def test_flt_x(self):
        with self.assertRaises(TypeError):
            Rectangle(3, 3, 2.2)

    def test_non_x(self):
        with self.assertRaises(TypeError):
            Rectangle(3, 3, None)

    def test_chr_x(self):
        with self.assertRaises(TypeError):
            Rectangle(3, 3, 'a')

    def test_str_x(self):
        with self.assertRaises(TypeError):
            Rectangle(3, 3, "UWU")

    def test_boo_x(self):
        with self.assertRaises(TypeError):
            Rectangle(3, 3, True)

    def test_lst_x(self):
        with self.assertRaises(TypeError):
            Rectangle(3, 3, [2, 2])

    def test_dic_x(self):
        with self.assertRaises(TypeError):
            Rectangle(3, 3, {"size": 1})

    def test_set_x(self):
        with self.assertRaises(TypeError):
            Rectangle(3, 3, {1, 1})

    def test_tup_x(self):
        with self.assertRaises(TypeError):
            Rectangle(3, 3, (1, 1))

    def test_ngv_x(self):
        with self.assertRaises(ValueError):
            Rectangle(3, 3, -3)

    def test_flt_y(self):
        with self.assertRaises(TypeError):
            Rectangle(3, 3, 3, 2.2)

    def test_non_y(self):
        with self.assertRaises(TypeError):
            Rectangle(3, 3, 3, None)

    def test_chr_y(self):
        with self.assertRaises(TypeError):
            Rectangle(3, 3, 3, 'a')

    def test_str_y(self):
        with self.assertRaises(TypeError):
            Rectangle(3, 3, 3, "UWU")

    def test_boo_y(self):
        with self.assertRaises(TypeError):
            Rectangle(3, 3, 3, True)

    def test_lst_y(self):
        with self.assertRaises(TypeError):
            Rectangle(3, 3, 3, [2, 2])

    def test_dic_y(self):
        with self.assertRaises(TypeError):
            Rectangle(3, 3, 3, {"size": 1})

    def test_set_y(self):
        with self.assertRaises(TypeError):
            Rectangle(3, 3, 3, {1, 1})

    def test_tup_y(self):
        with self.assertRaises(TypeError):
            Rectangle(3, 3, 3, (1, 1))

    def test_ngv_y(self):
        with self.assertRaises(ValueError):
            Rectangle(3, 3, 3, -3)

    def test_flt_w(self):
        with self.assertRaises(TypeError):
            Rectangle(3, 2.2)

    def test_non_w(self):
        with self.assertRaises(TypeError):
            Rectangle(3, None)

    def test_chr_w(self):
        with self.assertRaises(TypeError):
            Rectangle(3, 'a')

    def test_str_w(self):
        with self.assertRaises(TypeError):
            Rectangle(3, "UWU")

    def test_boo_w(self):
        with self.assertRaises(TypeError):
            Rectangle(3, True)

    def test_lst_w(self):
        with self.assertRaises(TypeError):
            Rectangle(3, [2, 2])

    def test_dic_w(self):
        with self.assertRaises(TypeError):
            Rectangle(3, {"size": 1})

    def test_set_w(self):
        with self.assertRaises(TypeError):
            Rectangle(3, {1, 1})

    def test_tup_w(self):
        with self.assertRaises(TypeError):
            Rectangle(3, (1, 1))

    def test_ngv_w(self):
        with self.assertRaises(ValueError):
            Rectangle(3, -3)

    def test_to_json(self):
        rekt1 = Rectangle(10, 5, 7, 2, 8)
        dict1 = rekt1.to_dictionary()
        dict2 = Base.to_json_string([dict1])
        self.assertEqual(len(str(dict1)) + 2, len(dict2))

    def test_get_w(self):
        rekt1 = Rectangle(8, 6, 7, 5, 1)
        self.assertEqual(8, rekt1.width)

    def test_get_h(self):
        rekt1 = Rectangle(8, 6, 7, 5, 1)
        self.assertEqual(6, rekt1.height)

    def test_get_x(self):
        rekt1 = Rectangle(8, 6, 7)
        self.assertEqual(7, rekt1.x)

    def test_get_y(self):
        rekt1 = Rectangle(8, 6, 7, 5)
        self.assertEqual(5, rekt1.y)

    def test_get_id(self):
        rekt1 = Rectangle(8, 6, 7, 5, 1)
        self.assertEqual(1, rekt1.id)

    def test_set_w(self):
        rekt1 = Rectangle(1, 1, 1, 1, 1)
        rekt1.width = 7
        self.assertEqual(7, rekt1.width)

    def test_set_h(self):
        rekt1 = Rectangle(1, 1, 1, 1, 1)
        rekt1.height = 7
        self.assertEqual(7, rekt1.height)

    def test_set_x(self):
        rekt1 = Rectangle(1, 1, 1)
        rekt1.x = 7
        self.assertEqual(7, rekt1.x)

    def test_set_y(self):
        rekt1 = Rectangle(1, 1, 1, 1)
        rekt1.y = 7
        self.assertEqual(7, rekt1.y)

    def test_set_id(self):
        rekt1 = Rectangle(1, 1, 1, 1, 1)
        rekt1.id = 7
        self.assertEqual(7, rekt1.id)

    def test_dic_bad(self):
        rekt1 = Rectangle(8, 6, 7, 5, 3)
        with self.assertRaises(TypeError):
            rekt1.to_dictionary(777)

    def test_str_bad(self):
        rekt1 = Rectangle(8, 6, 7, 5, 3)
        with self.assertRaises(TypeError):
            rekt1.__str__(777)

    def test_are_bad(self):
        rekt1 = Rectangle(8, 6, 7, 5, 3)
        with self.assertRaises(TypeError):
            rekt1.area(777)

    def test_dis_bad(self):
        rekt1 = Rectangle(8, 6, 7, 5, 3)
        with self.assertRaises(TypeError):
            rekt1.display(777)

    def test_jason_empty(self):
        dict1 = []
        js = Rectangle.to_json_string(dict1)
        self.assertEqual(len(js), 2)

    def test_jason_none(self):
        dict1 = None
        js = Rectangle.to_json_string(dict1)
        self.assertEqual(len(js), 2)

    def test_flt_reg(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(2.2, 2)

    def test_non_reg(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(None, 2)

    def test_chr_reg(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle('a', 2)

    def test_str_reg(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("UWU", 2)

    def test_boo_reg(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(True, 2)

    def test_lst_reg(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle([2, 2], 2)

    def test_dic_reg(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({"size": 1}, 2)

    def test_set_reg(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({1, 1}, 2)

    def test_tup_reg(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle((1, 1), 2)

    def test_ngv_reg(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-3, 2)

    def test_zed_reg(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 2)

    def test_flt_reg_h(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, 2.2)

    def test_non_reg_h(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, None)

    def test_chr_reg_h(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, 'a')

    def test_str_reg_h(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, "UWU")

    def test_boo_reg_h(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, True)

    def test_lst_reg_h(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, [2, 2])

    def test_dic_reg_h(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, {"size": 1})

    def test_set_reg_h(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, {1, 1})

    def test_tup_reg_h(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, (1, 1))

    def test_ngv_reg_h(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(2, -3)

    def test_zed_reg_h(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(2, 0)

    def test_flt_reg_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(2, 2, 2.2)

    def test_non_reg_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(2, 2, None)

    def test_chr_reg_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(2, 2, 'a')

    def test_str_reg_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(2, 2, "UWU")

    def test_boo_reg_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(2, 2, True)

    def test_lst_reg_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(2, 2, [2, 2])

    def test_dic_reg_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(2, 2, {"size": 1})

    def test_set_reg_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(2, 2, {1, 1})

    def test_tup_reg_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(2, 2, (1, 1))

    def test_ngv_reg_x(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(2, 2, -3)

    def test_flt_reg_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(2, 2, 2, 2.2)

    def test_non_reg_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(2, 2, 2, None)

    def test_chr_reg_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(2, 2, 2, 'a')

    def test_str_reg_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(2, 2, 2,"UWU")

    def test_boo_reg_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(2, 2, 2, True)

    def test_lst_reg_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(2, 2, 2, [2, 2])

    def test_dic_reg_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(2, 2, 2, {"size": 1})

    def test_set_reg_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(2, 2, 2, {1, 1})

    def test_tup_reg_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(2, 2, 2, (1, 1))

    def test_ngv_reg_y(self):
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(2, 2, 2, -3)

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

    def test_stf_rkt(self):
        rekt1 = Rectangle(1, 1, 1, 1, 1)
        Rectangle.save_to_file([rekt1])
        with open("Rectangle.json") as fred:
            self.assertEqual(len(fred.read()), 52)

    def test_stf_rkt_2(self):
        rekt1 = Rectangle(1, 1, 1, 1, 1)
        rekt2 = Rectangle(2, 2, 2, 2, 2)
        Rectangle.save_to_file([rekt1, rekt2])
        with open("Rectangle.json") as fred:
            self.assertEqual(len(fred.read()), 104)

    def test_stf_rkt_mpt(self):
        Rectangle.save_to_file([])
        with open("Rectangle.json") as fred:
            self.assertEqual(len(fred.read()), 2)

    def test_stf_rkt_non(self):
        Rectangle.save_to_file(None)
        with open("Rectangle.json") as fred:
            self.assertEqual(len(fred.read()), 2)

if __name__ == '__main__':
    unittest.main()
