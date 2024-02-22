#!/usr/bin/python3

# Write a function that prints a dictionary by ordered keys.
def print_sorted_dictionary(a_dictionary):

    for key in (a_dictionary):
        print("{}: {}". format(key, a_dictionary[key]))
