#!/usr/bin/python3
"""5. Save Object to a file"""
import json


def save_to_json_file(my_obj, filename):
    """ a function that writes an Object to a text file,
    using a JSON representation:"""

    with open(filename, "a", encoding="utf-8") as file:
        json.dump(my_obj, file)
