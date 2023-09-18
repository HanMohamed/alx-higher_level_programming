#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    new_multiplies_a = {}
    for key in a_dictionary:
        new_multiplies_a[key] = a_dictionary[key] * 2

    return (new_multiplies_a)
