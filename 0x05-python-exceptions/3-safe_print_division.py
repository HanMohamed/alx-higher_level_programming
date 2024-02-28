#!/usr/bin/python3

# Write a function that divides 2 integers and prints the result.
# The result of the division should print on the finally:
# section preceded by Inside result:
# Returns the value of the division, otherwise: None
# You have to use try: / except: / finally:
def safe_print_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result: {}".format(result))
    return result
