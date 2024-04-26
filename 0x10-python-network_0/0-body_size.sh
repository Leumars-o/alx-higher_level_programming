#!/bin/bash
# a bash script that takes a url, sends a request and displays the size of the body
curl -s "${1}" | wc -c
