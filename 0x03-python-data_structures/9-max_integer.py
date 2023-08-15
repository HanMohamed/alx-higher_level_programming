#!/usr/bin/python3

def max_integer(my_list=[]):

    if my_list is None:
        return None

    max_integer = my_list[0]
    for i in range(len(my_list)):
        if (my_list[i] > max_integer):
            max_integer = my_list[i]

    return max_integer
