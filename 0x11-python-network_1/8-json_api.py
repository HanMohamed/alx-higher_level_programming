#!/usr/bin/python3
""" Task: a Python script that takes in a letter
and sends a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter.
"""
import requests
import sys

if __name__ == "__main__":
    link = "http://0.0.0.0:5000/search_user"
    req = requests.get(link)
    # req = requests.post(link, data={'key': 'value'})

    # Check response body is JSON formatted
    if (req.json):
        if (len(sys.argv) == 2 and (sys.argv[1].isalpha())):
            req = requests.post(link, data={'q': sys.argv[1]})
            print(dict(req.text).get('id'))
            # print(dict(req.headers).get('name'))

        else:
            print('No result')
    else:
        print('Not a valid JSON')
