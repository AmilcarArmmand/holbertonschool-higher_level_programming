#!/bin/bash
# script that sends a JSON POST request to a URL with the filename as the second argument of the script
curl -sX POST -H "Content-type: application/json" -d "@$2" "$1"
