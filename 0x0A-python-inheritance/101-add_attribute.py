#!/usr/bin/python3
""" a single function defination """


def add_attribute(obj, att, value):
    """
    This function adds a new attribute to an object if it’s possible.
    """
    if hasattr(obj, "__dict__"):
        setattr(obj, att, value)
    else:
        raise TypeError("can't add new attribute")
