#!/usr/bin/python3
""" Write a class Square that defines a square by:
    - Private instance attribute: size:
        - property def size(self): to retrieve it
        - property setter def size(self, value): to set it:
            - size must be an integer, otherwise raise a TypeError
              exception with the message size must be an integer
            - if size is less than 0, raise a ValueError exception
              with the message size must be >= 0
    - Instantiation with optional size: def __init__(self, size=0):
    - Public instance method: def area(self): returns the current square area
    - Public instance method: def my_print(self): that prints in stdout
      the square with the character #:
      if size is equal to 0, print an empty line
"""


class Square:
    """Represent a Square"""

    def __init__(self, size=0):
        """Initialize a new square

        Args:
            size (int): the size of new square
        """

        self.__size = size

    @property
    def size(self):
        """ Retrieve size of square"""

        return (self.__size)

    @size.setter
    def size(self, value):
        """A setter function to set size of square"""

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns area of square"""

        return (self.__size * self.__size)

    def my_print(self):
        """ Printing a square"""

        if (self.__size == 0):
            print("")
        else:
            for i in range(0, self.__size):
                for j in range(0, self.__size):
                    print("#", end="")
                print("")
