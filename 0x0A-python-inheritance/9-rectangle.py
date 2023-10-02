#!/usr/bin/python3
"""
    A class Rectangle that inherits from BaseGeometry
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
        class Rectangle inherits from BaseGeometry
    """

    def __init__(self, width, height):
        """ private instantiation of attributes """

        super().integer_validator('width', width)
        super().integer_validator('height', height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """ Return rectangle description width and height """

        return ("[Rectangle] {:d}/{:d}".format(self.__width, self.__height))

    def area(self):
        """ Returns area of Rectangle instance """

        return (self.__width * self.__height)