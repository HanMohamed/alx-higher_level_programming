#!/usr/bin/python3
"""2. First Rectangle"""
from models.base import Base


class Rectangle(Base):
    """ class Rectangle that inherits from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self, width):
        self.__width = width

    @width.getter
    def width(self):
        return self.__width

    @property
    def height(self, height):
        self.__height = height

    @height.getter
    def height(self):
        return self.__height

    @property
    def x(self, x):
        self.__x = x

    @x.getter
    def x(self):
        return self.__x

    @property
    def y(self, y):
        self.__y = y

    @y.getter
    def y(self):
        return self.__y
