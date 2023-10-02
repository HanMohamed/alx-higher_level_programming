#!/usr/bin/python3
"""BaseGeometry class"""


class BaseGeometry:
    """Class BaseGeomentry"""

    def area(self):
        """raises an exception when called"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates value
        Param:
            name: name to validate
            value: value to validate
        Raises:
            TypeError: if value is not an int
            ValueError: if value is negative
        """

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0". format(name))
