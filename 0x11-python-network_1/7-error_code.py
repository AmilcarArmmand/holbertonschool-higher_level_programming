#!/usr/bin/python3
"""Python script sends request to URL and displays the body of the response
"""

import requests
from sys import argv


if __name__ == "__main__":
    r = requests.get(argv[1])
    if r.status_code.__ge__(400):
        print("Error code: {}".format(r.status_code))
    else:
        print(r.text)
