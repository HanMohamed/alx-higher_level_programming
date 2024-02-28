#!/usr/bin/python3
import sys


# Write a function that executes a function safely.
def safe_function(fct, *args):
    try:
        result = fct(*args)
    except Exception as err:
        result = None
        print("Exception:", err, file=sys.stderr)
    finally:
        return result
