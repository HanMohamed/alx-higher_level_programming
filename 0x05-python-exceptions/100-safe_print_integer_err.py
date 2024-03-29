#!/usr/bin/python3
import sys


# Write a function that prints an integer.
def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
    except Exception as err:
        print("Exception:", err, file=sys.stderr)
        return False
    else:
        return True
