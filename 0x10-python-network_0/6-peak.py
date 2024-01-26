#!/usr/bin/python3
""" find_peak """


def find_peak(list_of_integers):
    """find_peak
    Param:
        list_of_integers
    """
    if list_of_integers:
        list_of_integers.sort()
        return (list_of_integers[-1])

    return (None)
