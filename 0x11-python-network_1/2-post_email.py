#!/usr/bin/python3
""" Task:
"""
import urllib.request
import sys

if __name__ == "__main__":
    value = {'email' : sys.argv[2]}
    byte_value = urllib.parse.urlencode(value)
    byte_value = byte_value.encode('ascii')
    req = urllib.request.Request(sys.argv[1], value)
    with urllib.request.urlopen(sys.argv[1]) as response:
        html = response.read()
        print(html)
