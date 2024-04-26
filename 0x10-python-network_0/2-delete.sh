#!/bin/bash
# bash script that sends a DELETE request to the url passed as an argument
curl -s -X DELETE "${1}"
