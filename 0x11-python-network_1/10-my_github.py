#!/usr/bin/python3
""" Task: .
"""
import requests
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    link = "https://api.github.com/user/" + username
    # req = requests.post(link, data={'key': 'value'})
    req = requests.post(link, auth=(username, password))
    response = req.json()
    print((dict(response).get('id')))
