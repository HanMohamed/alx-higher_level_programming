#!/usr/bin/python3

is_lower = True

for i in range(122, 96, -1):
    if is_lower:
        is_lower = False
        x = i
    else:
        x = i - 32
        is_lower = True
    print("{}".format(chr(x)), end='')
