#!/usr/bin/python3
"""Define a square class"""


class Square:
    """ Define a square by size.

        Args:
            size: size of square.
    """
    def __init__(self, size=0):

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def size(self):
        """ Retrieve size
            Returns:
                size of square
        """

        return (self.__size)

    def size(self, value):
        """A setter function to set size of square"""

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """ Calculate square area

            Returns:
                square area
        """
        return (self.__size * self.__size)
