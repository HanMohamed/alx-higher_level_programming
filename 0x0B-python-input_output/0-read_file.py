#!/usr/bin/python3
"""0. Read file"""


def read_file(filename=""):
    """a function that reads a text file (UTF8) and prints it to stdout:"""
    with open(filename, encoding="utf-8") as file:
        data = file.read()
        print(data)
