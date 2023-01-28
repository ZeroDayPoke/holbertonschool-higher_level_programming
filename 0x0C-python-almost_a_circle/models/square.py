#!/usr/bin/python3
"""square module"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """square subclass of rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """get size property of square"""
        return self.width

    @size.setter
    def size(self, value):
        """set size prop"""
        self.width = value
        self.height = value

    def __str__(self):
        """rets sqr info"""
        strekt = "[Square] " + "({}) ".format(self.id)
        strekt += "{}/{} - ".format(self.x, self.y)
        strekt += "{}".format(self.width)
        return strekt

    def update(self, *args, **kwargs):
        """update sqr args"""
        if args:
            attrs = ["id", "size", "x", "y"]
            for ii in range(len(args)):
                setattr(self, attrs[ii], args[ii])
        else:
            for ky, vl in kwargs.items():
                setattr(self, ky, vl)

    def to_dictionary(self):
        """rets sqr richard"""
        richard = {"id": self.id,
                   "size": self.width, "x": self.x, "y": self.y}
        return richard
