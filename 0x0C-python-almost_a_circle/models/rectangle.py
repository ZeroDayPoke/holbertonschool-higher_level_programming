#!/usr/bin/python3
"""rectangle module"""
from models.base import Base


class Rectangle(Base):
    """rectangle subclass of base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        super().__init__(id)

    @property
    def width(self):
        """get width property of rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value

    @property
    def height(self):
        """get height property of rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value

    @property
    def x(self):
        """get x property of rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        """get y property of rectangle"""
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value
