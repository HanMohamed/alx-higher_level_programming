#!/usr/bin/python3
""" Error code #0
"""
import requests
import sys

if __name__ == "__main__":
    req = requests.get(sys.argv[1])
    if req.status_code > 400:
        print('Error code: {}'.format(req.status_code))
    print(req.text)
    