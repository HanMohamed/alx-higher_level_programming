#!/usr/bin/python3
"""Only sub class of"""


def inherits_from(obj, a_class):
    """True if the object is exactly an instance of the specified class"""
    return (issubclass(type(obj), a_class) and type(obj) != a_class)
