#!/usr/bin/python3
"""
Write a class Rectangle that inherits from BaseGeometry (7-base_geometry.py). (task based on 8-rectangle.py)

Instantiation with width and height: def __init__(self, width, height)::
width and height must be private. No getter or setter
width and height must be positive integers validated by integer_validator
the area() method must be implemented
print() should print, and str() should return, the following rectangle description: [Rectangle] <width>/<height>
BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""


class Rectangle(BaseGeometry):
    """da rect subclass of base geo"""
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def area(self):
        """area of rectangle is width * height"""
        return self.__width * self.__height

    def __str__(self):
        """str representation of Rectangle"""
        rect_string = "[Rectangle] "
        rect_string += str(self.__width) + "/" + str(self.__height)
        return rect_string
