#!/usr/bin/python3
""" Task: POST an email #1
"""
import requests
import sys

if __name__ == "__main__":
    value = {'email': sys.argv[2]}
    response = requests.post(sys.argv[1], value)
    html = response.text
    print(html)
