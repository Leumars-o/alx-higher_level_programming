#!/usr/bin/python3
"""A python script that sends a POST request to a URL.
    with a given data as parameter
"""
import requests
import sys

if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    q = sys.argv[1] if len(sys.argv) > 1 else ""
    data = {"q": q}
    response = requests.post(url, data=data)
    r_type = response.headers["Content-Type"]
    if r_type == "application/json":
        result = response.json()
        r_id = result.get('id')
        name = result.get('name')
        if (result and r_id and name):
            print(f"[{r_id}] {name}")
        else:
            print("No result")
    else:
        print("Not a valid JSON")
