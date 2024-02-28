#!/usr/bin/python3
""" Write a class Square that defines a square by:
    - Private instance attribute: size
    - Instantiation with size (no type/value verification)
"""


class Square:
    """Represent a Square"""

    def __init__(self, size):
        """Initialize a new square

        Args:
            size (int): the size of new square
        """
        self.__size = size
