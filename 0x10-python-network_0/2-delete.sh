#!/bin/bash
# sends DELETE request to URL passed as argument, displays body of the response
curl -sX DELETE "$1"
