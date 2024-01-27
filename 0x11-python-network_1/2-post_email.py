#!/usr/bin/python3
""" Task:
"""
import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    value = {'email' : sys.argv[2]}
    # data should be bytes
    byte_value = value.encode('ascii')
    req = urllib.request.Request(sys.argv[1], byte_value)
    with urllib.request.urlopen(req) as response:
        html = response.read()
        print(html.decode('utf-8'))
