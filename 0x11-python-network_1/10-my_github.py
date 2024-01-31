#!/usr/bin/python3
""" Task: .
"""
import requests
import sys

if __name__ == "__main__":
    link = "https://api.github.com/user"
    # req = requests.post(link, data={'key': 'value'})
    req = requests.get(link, data={sys.argv[1], sys.argv[2]})
    print((dict(req).get('id')))
