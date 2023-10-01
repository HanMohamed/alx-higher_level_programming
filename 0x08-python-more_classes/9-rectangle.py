#!/usr/bin/python3
"""Define a Rectangle class"""


class Rectangle:
    """ Represent a Rectangle.
    Attributes:
        number_of_instances (int): The number of Rectangle instances.
        print_symbol: # symbol
    """

    number_of_instances = 0
    print_symbol = "#"

    @classmethod
    def square(cls, size=0):
        """ Returns a new instance of Rectangle """
        return cls(size, size)

    def __init__(self, width=0, height=0):
        """ Initialize a new Rectangle.

        Args:
            width : width
            height : height
        """
        self.__width = width
        self.__height = height
        type(self).number_of_instances += 1

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

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif (value < 0):
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

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif (value < 0):
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ returns the rectangle area"""
        return (self.__height * self.__width)

    def perimeter(self):
        """ returns the rectangle perimeter"""
        if (self.__height == 0 or self.__width == 0):
            return (0)

        return (2 * (self.__height + self.__width))

    def __str__(self):
        """ print the rectangle with the character #"""
        if (self.__height == 0 or self.__width == 0):
            return ("")
        print_rect = ""
        for i in range(0, self.__height):
            for j in range(0, self.__width):
                print_rect += str(self.print_symbol)
            if (i != self.__height - 1):
                print_rect += "\n"
        return (print_rect)

    def __repr__(self):
        """ Return the string representation of the Rectangle."""
        print_rect = "Rectangle(" + str(self.__width)
        print_rect += ", " + str(self.__height) + ")"
        return (print_rect)

    def __del__(self):
        type(self).number_of_instances -= 1
        """Print a message for every deletion of a Rectangle."""
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ rect_1 and rect_2 must be instance of rectangle class """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        elif rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
