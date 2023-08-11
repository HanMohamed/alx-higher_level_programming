#!/usr/bin/python3

if __name__ == "__main__":
    import sys

num = len(sys.argv) - 1
sum = 0

for i in range(0, num):
    sum += int(sys.argv[i + 1])
print("{}".format(sum))
