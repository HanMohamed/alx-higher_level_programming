#!/usr/bin/python3
"""2. First Rectangle"""
from models.base import Base


class Rectangle(Base):
    """ class Rectangle that inherits from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """returns the area value of the Rectangle instance."""

        return self.__height * self.__width

    def display(self):
        """prints in stdout the Rectangle instance with the character # """

        for i in range(self.__height):
            for j in range(self.__width):
                print("#", end='')
            print()

    def __str__(self):
        """returns [Rectangle] (<id>) <x>/<y> - <width>/<height>"""

        rec = "[Rectangle] (" + str(self.id) + ") "
        rec += str(self.__x) + "/" + str(self.__y) + " - "
        rec += str(self.__width) + "/" + str(self.__height)
        return rec

    def display(self):
        """print in stdout the Rectangle instance
        with the character # by taking care of x and y"""

        for i in range(self.__y):
            print()
        for i in range(self.__height):
            for j in range(self.__x):
                print(" ", end='')
            for j in range(self.__width):
                print("#", end='')
            print()

    def update(self, *args, **kwargs):
        """assigns an argument to each attribut"""
        if args:
            list_args = ["id", "width", "height", "x", "y"]
            for i in range(len(args)):
                setattr(self, list_args[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)
