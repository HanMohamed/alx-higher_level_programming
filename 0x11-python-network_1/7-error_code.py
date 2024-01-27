#!/usr/bin/python3
""" Error code #0
"""
import requests
import sys

if __name__ == "__main__":
    try:
      req = requests.get(sys.argv[1])
    except requests.error.HTTPError as response:
        print('Error code: {}'.format(response))
    else:
        print(req.text)
