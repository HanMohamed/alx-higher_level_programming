#!/usr/bin/python3

if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys

if len(sys.argv != 4):
    print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    exit(1)

a = int(sys.argv[2])
b = int(sys.argv[4])
sign = str(sys.argv[3])

match sign:
    case "+":
        print("{0} + {1} = {2}".format(a, b, add(a, b)))
    case "-":
        print("{0} - {1} = {2}".format(a, b, sub(a, b)))
    case "*":
        print("{0} * {1} = {2}".format(a, b, mul(a, b)))
    case "/":
        print("{0} / {1} = {2}".format(a, b, div(a, b)))
