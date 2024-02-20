#!/usr/bin/python3

# Write a program that imports functions from the file calculator_1.py,
# does some Maths, and prints the result.

# Do not use the function print (with string format to display integers)
# more than 4 times
# You have to define:
# the value 10 to a variable a
# the value 5 to a variable b
# and use those two variables only, as arguments when calling functions
# a and b must be defined in 2 different lines: a = 10 and another b = 5
# Your program should call each of the imported functions.
# the word calculator_1 should be used only once in your file
# You are not allowed to use * for importing or __import__
# Your code should not be executed when imported

if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div

    a = 10
    b = 5

    print("{0} + {1} = {2}".format(a, b, add(a, b)))
    print("{0} - {1} = {2}".format(a, b, sub(a, b)))
    print("{0} * {1} = {2}".format(a, b, mul(a, b)))
    print("{0} / {1} = {2}".format(a, b, div(a, b)))
