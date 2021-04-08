#!/bin/bash
# sends a GET request to the URL with header variable value of 98
curl -sX GET -H "X-HolbertonSchool-User-Id: 98" "$1"
