#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    if my_list is None:
        return None

    copy_list = []
    for i in range(len(my_list)):
        copy_list.append(my_list[i])

    if (idx < 0 or idx >= len(my_list)):
        return copy_list

    copy_list[idx] = element
    return copy_list
