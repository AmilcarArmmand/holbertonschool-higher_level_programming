#!/usr/bin/python3
"""Python script that takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user with the letter as a parameter.
"""

import requests
from sys import argv


if __name__ == "__main__":
    if len(argv).__eq__(2):
        q = argv[1]
    else:
        q = ""
    r = requests.post('http://0.0.0.0:5000/search_user', data={'q': q})
    try:
        j = r.json()
        id = j.get('id')
        name = j.get('name')
        if len(j).__eq__(0) or not id or not name:
            print("No result")
        else:
            print("[{}] {}".format(j.get('id'), j.get('name')))
    except:
        print("Not a valid JSON")
