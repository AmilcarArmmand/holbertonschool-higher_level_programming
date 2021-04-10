#!/usr/bin/python3
"""Python script that takes your GitHub credentials (username and password)
"""

import requests
from sys import argv


if __name__ == "__main__":
    r = requests.get("https://api.github.com/repos/{}/{}/commits"
                     .format(argv[2], argv[1]))
    commits = r.json()
    for commit in commits[:10]:
        print(commit.get('sha'), end=': ')
        print(commit.get('commit').get('author').get('name'))
