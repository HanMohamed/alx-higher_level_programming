#!/usr/bin/python3
""" Task: What's my status? #1
"""
import requests

if __name__ == "__main__":
    req = requests.get('https://alx-intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type: {}".format(type(req)))
    print("\t- content: {}".format(req.content))
