#!/usr/bin/python3
"""still square like in nature"""


class Square:
    """in moar powerful square square can print square"""
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, valx):
        if not isinstance(valx, int):
            raise TypeError("size must be an integer")
        elif valx < 0:
            raise ValueError("size must be >= 0")
        self.__size = valx

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for ii in range(self.__size):
                for ij in range(self.__size):
                    print("#", end="")
                print()
