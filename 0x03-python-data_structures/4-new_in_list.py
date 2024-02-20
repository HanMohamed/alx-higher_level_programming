#!/usr/bin/python3

# Write a function that replaces an element in a list at a specific position
# without modifying the original list (like in C).
def new_in_list(my_list, idx, element):
    if my_list is None:
        return None

    copy_list = my_list.copy()

    if (idx < 0 or idx >= len(my_list)):
        return copy_list

    copy_list[idx] = element
    return copy_list
