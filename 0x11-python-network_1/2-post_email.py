#!/usr/bin/python3
"""Python script that takes in a URL and an email, sends a POST request
and displays the body of the response (decoded in utf-8)

"""

import urllib.parse
import urllib.request
import sys


if __name__ == "__main__":
    values = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(values).encode('utf-8')
    req = urllib.request.Request(sys.argv[1], data)
    with urllib.request.urlopen(req) as response:
        print(response.read().decode('utf-8'))
