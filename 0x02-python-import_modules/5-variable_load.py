#!/usr/bin/python3
# Write a program that imports the variable a from the file variable_load_5.py
# and prints its value.
# You are not allowed to use * for importing or __import__
# Your code should not be executed when imported

if __name__ == "__main__":
    from variable_load_5 import a
    print("{}".format(a))
