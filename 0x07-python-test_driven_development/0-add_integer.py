#!/usr/bin/python3
"""a function that adds 2 integers"""


def add_integer(a, b=98):
    """ a function that adds 2 integers

    Args:
        a (int): number
        b (int, optional): number. Defaults to 98.

    Raises:
        TypeError: number must be integer or float
        TypeError: number must be integer or float

    Returns:
        sum
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")

    return int(a) + int(b)
