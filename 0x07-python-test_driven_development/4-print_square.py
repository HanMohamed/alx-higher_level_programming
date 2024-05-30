#!/usr/bin/python3
""" A  function that prints a square with the character #."""


def print_square(size):
    """a function that prints a square with the character #

    Args:
        size (int): number

    Raises:
        TypeError: size must be an integer
        ValueError: size must be >= 0
        TypeError: size must be an integer
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
