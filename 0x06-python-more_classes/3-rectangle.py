#!/usr/bin/python3
"R3K7 Rect"


class Rectangle:
    "sassy classy"
    def __init__(self, width=0, height=0):
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._height = value

    def perimeter(self):
        if self._width == 0 or self._height == 0:
            return 0
        return 2 * (self._width + self._height)

    def area(self):
        return self._width * self._height

    def __str__(self):
        if self._width == 0 or self._height == 0:
            return ""
        rektrect = "#" * self._width + "\n"
        rektrect = rektrect * self._height
        return rektrect

    def __repr__(self):
        return "Rectangle({}, {})".format(self._width, self._height)
