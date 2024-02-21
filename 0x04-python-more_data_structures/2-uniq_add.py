#!/usr/bin/python3

# Write a function that adds all unique integers
# in a list (only once for each integer).
def uniq_add(my_list=[]):
    sum_list = 0
    for i in set(my_list):
        sum_list += i
    return (sum_list)
