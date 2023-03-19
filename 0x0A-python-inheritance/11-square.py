#!/usr/bin/python3
"""
Write a class Square that inherits from Rectangle (9-rectangle.py). (task based on 10-square.py).

Instantiation with size: def __init__(self, size)::
size must be private. No getter or setter
size must be a positive integer, validated by integer_validator
the area() method must be implemented
print() should print, and str() should return, the square description: [Square] <width>/<height>
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """square is also a rectangle"""
    def __init__(self, size):
        """instantiates Square subclass"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """string representation of Square"""
        square_string = "[Square] "
        square_string += str(self.__size) + "/" + str(self.__size)
        return square_string
