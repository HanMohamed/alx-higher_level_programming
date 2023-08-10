#!/usr/bin/python3

def pow(a, b):

    if b == 0:
        return 1

    if b < 0:
        a = 1 / a
        b = b * -1

    result = a
    while b > 1:
        result = result * a
        b = b - 1

    return result
