#!/usr/bin/python3
""" Task: POST an email #0
"""
import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    value = {'email': sys.argv[2]}
    # data should be parsed first to be bytes
    byte_value = urllib.parse.urlencode(value)
    # data should be bytes
    byte_value = byte_value.encode('ascii')
    # passing arg means 'POST'
    req = urllib.request.Request(sys.argv[1], byte_value)
    with urllib.request.urlopen(req) as response:
        html = response.read()
        # the response (decoded in utf-8)
        print(html.decode('utf-8'))
