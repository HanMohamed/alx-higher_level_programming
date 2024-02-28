#!/usr/bin/python3

# a function that prints the first x elements of a list and only integers.
# my_list can contain any type (integer, string, etc.)
# All integers have to be printed on the same line followed by a new line
#  - other type of value in the list must be skipped (in silence).
# x represents the number of elements to access in my_list
# x can be bigger than the length of my_list - if it’s the case:
# an exception is expected to occur
# Returns the real number of integers printed
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
        except (ValueError, TypeError):
            continue
        else:
            count += 1
    print()
    return count
