#!/usr/bin/python3
""" Task: .
"""
import requests
import sys

if __name__ == "__main__":
    link = "https://api.github.com/user"
    # req = requests.post(link, data={'key': 'value'})
    head = {sys.argv[1], sys.argv[2]}
    req = requests.get(link, headers=head)
    print((dict(req).get('id')))
