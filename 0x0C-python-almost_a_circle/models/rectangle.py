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
        """set width prop"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """get height property of rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """set height prop"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """get x property of rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        """set x prop"""
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """get y property of rectangle"""
        return self.__y

    @y.setter
    def y(self, value):
        """set y prop"""
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """area of rect is len * width"""
        return self.width * self.height

    def display(self):
        """prints rect to stdout"""
        rektrect = '\n' * self.y
        rektrect += (' ' * self.x + '#' * self.width + '\n') * self.height
        rektrect = rektrect[:-1]
        print(rektrect)

    def __str__(self):
        """rets rect info"""
        strekt = "[Rectangle] " + "({}) ".format(self.id)
        strekt += "{}/{} - ".format(self.x, self.y)
        strekt += "{}/{}".format(self.width, self.height)
        return strekt

    def update(self, *args, **kwargs):
        """meth updates args"""
        if args:
            attrs = ["id", "width", "height", "x", "y"]
            for ii in range(len(args)):
                setattr(self, attrs[ii], args[ii])
        for ky, vl in kwargs.items():
            setattr(self, ky, vl)

    def to_dictionary(self):
        """rets rect richard"""
        richard = {"id": self.id, "width": self.width,
                   "height": self.height, "x": self.x, "y": self.y}
        return richard
