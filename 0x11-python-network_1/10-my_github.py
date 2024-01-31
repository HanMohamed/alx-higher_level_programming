#!/usr/bin/python3
""" Task: .
"""
import requests
import sys

if __name__ == "__main__":
    link = "https://docs.github.com/en/rest/users?apiVersion=2022-11-28"
    # req = requests.post(link, data={'key': 'value'})
    username = sys.argv[1]
    password = sys.argv[2]
    head = {username, password}
    req = requests.get(link, headers=head)
    print("[{}] {}".format(dict(req).get('id')))
