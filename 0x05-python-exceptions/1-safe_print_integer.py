#!/usr/bin/python3

# Write a function that prints an integer with "{:d}".format().
# Returns True if value has been correctly printed
# (it means the value is an integer)
# Otherwise, returns False
# You have to use "{:d}".format() to print as integer
def safe_print_integer(value):
    try:
        print("{:d}".format(value))
    except Exception:
        return False
    else:
        return True
