#!/usr/bin/python3
"""Rebel Int-heritance"""


class MyInt(int):
    """MyInt Class Module"""
    def __eq__(self, other):
        """overrides == operator"""
        return not super().__eq__(other)
    
    def __ne__(self, other):
        """overrides != operator"""
        return super().__eq__(other)
