#!/usr/bin/python3
"""The Square Module"""


class Square:
    """Defines a class named Square"""
    def __init__(self, size=0):
        """
        Initialize the square object with a size
        Args:
            size (int): the size of one side of Square
        """
        self.size = size

    @property
    def size(self):
        """Square size property getter"""
        return self.__size

    @size.setter
    def size(self, valx):
        """Square size property setter"""
        if not isinstance(valx, int):
            raise TypeError("size must be an integer")
        elif valx < 0:
            raise ValueError("size must be >= 0")
        self.__size = valx

    def area(self):
        """Returns the area of a Square (its size squared)"""
        return self.__size ** 2

    def my_print(self):
        """prints visual representation of Square"""
        if self.__size == 0:
            print()
        else:
            for ii in range(self.__size):
                for ij in range(self.__size):
                    print("#", end="")
                print()
