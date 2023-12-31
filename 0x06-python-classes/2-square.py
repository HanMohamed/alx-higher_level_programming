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
