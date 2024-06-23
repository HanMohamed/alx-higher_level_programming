#!/usr/bin/python3
"""
   A class Square that inherits from BaseGeometry
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Class Square inherits from 9-rectangle """

    def __init__(self, size):
        """Instantiate private instance size"""

        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """ Return square description width and height """

        return "[Square] {:d}/{:d}".format(self.__size, self.__size)
