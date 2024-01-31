#!/usr/bin/python3
""" Task: .
"""
import requests
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    link = "https://api.github.com/users/" + username
    # req = requests.post(link, data={'key': 'value'})
    req = requests.get(link, auth=(username, password),
                       headers={'Authorization': password})
    response = req.json()
    print((dict(response).get('id')))
