#!/usr/bin/python3
""" Task: POST an email #0
"""
import requests
import sys

if __name__ == "__main__":
    value = {'email': sys.argv[2]}
    # data should be parsed first to be bytes
    byte_value = requests.parse.urlencode(value)
    # data should be bytes
    byte_value = byte_value.encode('ascii')
    # passing arg means 'POST'
    req = requests.Request(sys.argv[1], byte_value)
    response = requests.get(req)
    html = response.read()
    # the response (decoded in utf-8)
    print(html.decode('utf-8'))
