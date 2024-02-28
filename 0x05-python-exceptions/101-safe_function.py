#!/usr/bin/python3
import sys


# Write a function that executes a function safely.
# You can assume fct will be always a pointer to a function
# Returns the result of the function,
# Otherwise, returns None if something happens during the function
# and prints in stderr the error precede by Exception:
def safe_function(fct, *args):
    try:
        result = fct(*args)
    except Exception as err:
        result = None
        print("Exception:", err, file=sys.stderr)
    finally:
        return result
