#!/usr/bin/python3
"""Python script that takes a URL and email,
sends a post request to the URL with email as parameter,
and prints the response decoded in (utf-8)
"""
import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    data = urllib.parse.urlencode({'email': email})
    with urllib.request.urlopen(url, data.encode('ascii')) as resp:
        print(resp.read().decode('utf-8'))
