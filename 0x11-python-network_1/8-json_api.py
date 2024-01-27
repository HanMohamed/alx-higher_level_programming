#!/usr/bin/python3
""" Task:
"""
import requests
import sys

if __name__ == "__main__":
    req = requests.get(sys.argv[1])
    print(req)
