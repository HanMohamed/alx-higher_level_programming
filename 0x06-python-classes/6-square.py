#!/usr/bin/python3
"""Define a square class"""


class Square:
    """ Define a square by size.

        Args:
            size: size of square.
            position:
    """
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """ Retrieve size
            Returns:
                size of square
        """

        return (self.__size)

    @property
    def position(self):
        """ Retrieve position
            Returns:
                position of square
        """
        return (self.__position)

    @size.setter
    def size(self, value):
        """A setter function to set size of square
            Args:
                value: size of square.
        """

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @position.setter
    def position(self, value):
        """ Set position

        Args:
            value: must be a tuple of 2 positive integers.

        Raises:
            TypeError: must be a tuple of 2 positive integers.
        """

        if not isinstance(value, tuple(int, int)):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """ Calculate square area

            Returns:
                square area
        """
        return (self.__size * self.__size)

    def my_print(self):
        if (self.__size == 0):
            print("")
        else:
            for i in range(0, self.__size):
                for j in range(0, self.__position[0]):
                    if self.__position[1] == 0:
                        print(" ", end="")
                for j in range(0, self.__size):
                    print("#", end="")
                print("")
