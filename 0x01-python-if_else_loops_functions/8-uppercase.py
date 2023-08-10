#!/usr/bin/python3

def uppercase(str):
    STR = ""
    for i in str:
        if ord(i) in range(97, 123):
            x = ord(i) - 32
            STR += chr(x)
        else:
            STR += i
    print("{}".format(STR))
