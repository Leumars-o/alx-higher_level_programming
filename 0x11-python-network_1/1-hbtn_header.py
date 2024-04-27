#!/usr/bin/python3
"""Python script that takes in a url as an argument,
    and then sends a request to the URL,
    and displays the value of the X-Request-Id
"""
import urllib.request as r
import sys

if __name__ == "__main__":
    request = r.Request(sys.argv[1])
    with r.urlopen(request) as response:
        print(response.info()["X-Request-Id"])
