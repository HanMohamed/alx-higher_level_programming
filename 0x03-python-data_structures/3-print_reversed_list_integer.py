#!/usr/bin/python3

# Write a function that prints all integers of a list, in reverse order.
def print_reversed_list_integer(my_list=[]):
    if (my_list is None):
        return

    my_list.reverse()
    for i in (my_list):
        print("{:d}".format(i))
    my_list.reverse()
