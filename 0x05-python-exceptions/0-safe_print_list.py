#!/usr/bin/python3

# Write a function that prints x elements of a list.
# my_list can contain any type (integer, string, etc.)
# All elements must be printed on the same line followed by a new line.
# x represents the number of elements to print
# x can be bigger than the length of my_list
# Returns the real number of elements printed
def safe_print_list(my_list=[], x=0):
    i = 0
    while i < x:
        try:
            print(my_list[i], end='')
        except Exception:
            break
        else:
            i += 1

    print()
    return i
