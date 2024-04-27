#!/usr/bin/python3
"""Python script that takes in a URL as an argument,
sends a request to the URL and displays the body of the response.
"""
import sys
import urllib.error as err
import urllib.request as r

if __name__ == "__main__":
    url = sys.argv[1]
    try:
        with r.urlopen(url) as response:
            print(response.read().decode("utf-8"))
    except err.HTTPError as e:
        print(f"Error code: {e.code}")
