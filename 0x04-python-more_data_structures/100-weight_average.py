#!/usr/bin/python3

# Write a function that returns the weighted average of all integers
# tuple (<score>, <weight>)
# Returns 0 if the list is empty
def weight_average(my_list=[]):
    if not my_list:
        return 0
    numerator = sum(map(lambda x, y: x[0] * y[1], my_list, my_list))
    denomerator = sum(map(lambda x: x[1], my_list))
    return numerator / denomerator
