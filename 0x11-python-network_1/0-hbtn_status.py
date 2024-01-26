#!/usr/bin/python3
if __name__ == "__main__":
    import urllib.request
    link = 'https://alx-intranet.hbtn.io/status'
    with urllib.request.urlopen(link) as response:
        html = response.read()
    print(html)
