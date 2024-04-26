#!/bin/bash
#bash script thats sends a reques to a url passed as an argument and displays the status code
curl -s -o /dev/null -w "%{http_code}" "${1}"
