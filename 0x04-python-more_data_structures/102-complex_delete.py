#!/usr/bin/python3

# Write a function that deletes keys with a specific value in a dictionary.
# If the value doesn’t exist, the dictionary won’t change
# All keys having the searched value have to be deleted
# You are not allowed to import any module
def complex_delete(a_dictionary, value):
    all_values = list(a_dictionary.values())
    if value not in all_values:
        return
    for i in range(0, len(all_values)):
        print(all_values[i])
        if value == all_values[i]:
            print(all_values[i])