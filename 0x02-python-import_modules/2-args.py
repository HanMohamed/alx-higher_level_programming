#!/usr/bin/python3

if __name__ == "__main__":
    import sys

num = len(sys.argv) - 1
if num == 0:
    print("{} arguments.".format(num))

elif num == 1:
    print("{} argument:".format(num))
    print("{}: {}".format(1, sys.argv[1]))

else:
    print("{} argumens:".format(num))
    for i in range(0, num):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
