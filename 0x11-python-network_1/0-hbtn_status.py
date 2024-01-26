#!/usr/bin/python3

import urllib.request
if __name__ == "__main__":
    link = 'https://alx-intranet.hbtn.io/status'
    with urllib.request.urlopen(link) as response:
        html = response.read()
    print(html)
