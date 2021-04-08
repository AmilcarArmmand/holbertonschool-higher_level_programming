#!/bin/bash
# script sends request to URL and displays only the status code of the response
curl -o /dev/null -sw %"{http_code}" "$1"
