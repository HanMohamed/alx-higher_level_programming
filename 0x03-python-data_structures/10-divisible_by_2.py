#!/usr/bin/python3

# Write a function that finds all multiples of 2 in a list.
def divisible_by_2(my_list=[]):
    divisible_list = []

    for i in my_list:
        if (i % 2 == 0):
            divisible_list.append(True)
        else:
            divisible_list.append(False)

    return divisible_list
