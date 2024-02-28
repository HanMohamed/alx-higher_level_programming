#!/usr/bin/python3
""" Write a class Square that defines a square by:
    - Private instance attribute: size:
        - property def size(self): to retrieve it
        - property setter def size(self, value): to set it:
            - size must be an integer, otherwise raise a TypeError
              exception with the message size must be an integer
            - if size is less than 0, raise a ValueError exception
              with the message size must be >= 0
    - Private instance attribute: position:
        - property def position(self): to retrieve it
        - property setter def position(self, value): to set it:
            - position must be a tuple of 2 positive integers,
              otherwise raise a TypeError exception with the message:
              position must be a tuple of 2 positive integers
    - Instantiation with optional size:
      def __init__(self, size=0, position=(0, 0)):
    - Public instance method: def area(self): returns the current square area
    - Public instance method: def my_print(self): that prints in stdout
      the square with the character #:
        - if size is equal to 0, print an empty line
        - position should be use by using space
          Don't fill lines by spaces when position[1] > 0
"""


class Square:
    """Represent a Square"""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new square

        Args:
            size (int): the size of new square
            position (tuple): the position of square
        """

        self.__size = size
        self.__position = position

    @property
    def size(self):
        """ Retrieve size of square"""

        return (self.__size)

    @property
    def position(self):
        """ Retrieve position of square"""

        return (self.__position)

    @size.setter
    def size(self, value):
        """A setter function to set size of square"""

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @position.setter
    def position(self, value):
        """A setter function to set position of square"""

        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Returns area of square"""

        return (self.__size * self.__size)

    def my_print(self):
        """ Printing a square"""

        if (self.__size == 0):
            print("")
        else:
            for i in range(0, self.__position[1]):
                print("")
            for i in range(0, self.__size):
                for j in range(0, self.__position[0]):
                    print(" ", end="")
                for j in range(0, self.__size):
                    print("#", end="")
                print("")
