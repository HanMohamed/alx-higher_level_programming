#!/usr/bin/python3

# Write a program that prints the result of the addition of all arguments
# The output should be the result of the addition of all arguments,
# followed by a new line
# You can cast arguments into integers by using int()
# (you can assume that all arguments can be casted into integers)
# Your code should not be executed when imported

if __name__ == "__main__":
    import sys

    num = len(sys.argv) - 1
    sum = 0

    for i in range(0, num):
        sum += int(sys.argv[i + 1])
    print("{}".format(sum))
