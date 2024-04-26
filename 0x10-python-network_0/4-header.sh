#!/bin/bash
# bash script that takes a url arg, and sends a GET request to it
curl -s -H "X-School-User-Id: 98" -X GET "$1"
