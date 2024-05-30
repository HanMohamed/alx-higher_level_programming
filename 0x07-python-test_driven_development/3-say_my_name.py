#!/usr/bin/python3
"""
A function that prints My name is <first name> <last name>
"""


def say_my_name(first_name, last_name=""):
    """
    a function that prints My name is <first name> <last name>

    Args:
        first_name (str): first_name
        last_name (str, optional): last_name

    Raises:
        TypeError: first_name must be a string
        TypeError: last_name must be a string
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
