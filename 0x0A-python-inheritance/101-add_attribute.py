#!/usr/bin/python3
"""attribute adder"""


def add_attribute(obj, attr, value):
    """
    adds attribute w/ value to object
    Args:
        obj (any): target object
        attr (any): attribute to add
        value (any): value of attr
    """
    if hasattr(obj, attr):
        """Check if the object already has the attribute"""
        obj.__dict__[attr] = value
    else:
        """Raise a TypeError exception if the object can't have new attributes"""
        if not hasattr(obj, '__dict__'):
            msg = "can't add new attribute"
            raise TypeError(msg)
        """Add the new attribute to the object"""
        setattr(obj, attr, value)
