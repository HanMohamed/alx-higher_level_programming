#!/usr/bin/python3
""" Task:
"""
import urllib.requests
import sys

if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as response:
        print(response)
