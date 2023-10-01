#!/usr/bin/python3
"""Define a square class"""


class Rectangle:
    """ Define a square by size.

        Args:
            size: size of square.
    """
    def __init__(self, width=0, height=0):

        self.__width = width
        self.__height = height

    @property
    def width(self):
        """ Retrieve width
            Returns:
                width of rectangle
        """
        return (self.__width)

    @width.setter
    def width(self, value):
        """A setter function to set width of rectangle"""

        if type(value) is not int:
            raise TypeError("width must be an integer")
        if (value < 0):
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Retrieve height
            Returns:
                height of rectangle
        """
        return (self.__height)

    @height.setter
    def height(self, value):
        """A setter function to set height of rectangle"""

        if type(value) is not int:
            raise TypeError("height must be an integer")
        if (value < 0):
            raise ValueError("height must be >= 0")
        self.__height = value
