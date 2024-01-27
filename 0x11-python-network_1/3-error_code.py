#!/usr/bin/python3
""" Error code #0
"""
import urllib.request
import urllib.error
import sys

if __name__ == "__main__":
    req = urllib.request.Request(sys.argv[1])
    try:
        with urllib.request.urlopen(req) as response:
            html = response.read()
    except urllib.error.HTTPError as response:
        print('Error code: {}'.format(response.code))
    else:
        print(html.decode('utf-8'))
