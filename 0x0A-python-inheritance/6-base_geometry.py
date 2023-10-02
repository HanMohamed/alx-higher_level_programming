#!/usr/bin/python3
"""Base Geometry class"""


class BaseGeometry:
    """A class with public attribute area"""

    def area(self):
        """raises an exception when called"""
        raise Exception("area() is not implemented")
