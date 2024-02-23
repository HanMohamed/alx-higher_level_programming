#!/usr/bin/python3

# Write a function that deletes keys with a specific value in a dictionary.
# If the value doesn’t exist, the dictionary won’t change
# All keys having the searched value have to be deleted
# You are not allowed to import any module
def complex_delete(a_dictionary, value):
    all_values = list(a_dictionary.values())
    all_keys = list(a_dictionary.keys())

    if value not in all_values:
        return a_dictionary
    for i in range(0, len(all_values)):
        if value == all_values[i]:
            del [a_dictionary[all_keys[i]]]
    return a_dictionary
