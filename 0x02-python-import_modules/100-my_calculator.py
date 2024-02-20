#!/usr/bin/python3
# Write a program that imports all functions from the file calculator_1.py
# and handles basic operations.

from calculator_1 import add, sub, mul, div
import sys

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    a = int(sys.argv[1])
    b = int(sys.argv[3])
    sign = sys.argv[2]

    if sign == '+':
        print("{0} + {1} = {2}".format(a, b, add(a, b)))
    elif sign == '-':
        print("{0} - {1} = {2}".format(a, b, sub(a, b)))
    elif sign == '*':
        print("{0} * {1} = {2}".format(a, b, mul(a, b)))
    elif sign == '/':
        print("{0} / {1} = {2}".format(a, b, div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
