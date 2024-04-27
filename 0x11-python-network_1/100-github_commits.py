#!/usr/bin/python3
"""A python script that lists the last 10 commits to a GitHub repository.
"""
import requests
import sys

if __name__ == "__main__":
    rep_name = sys.argv[1]
    user_name = sys.argv[2]
    url = "https://api.github.com/repos/"
    + user_name + "/" + rep_name + "/commits"
    response = requests.get(url)
    json = response.json()

    for commit in json[::-1][:10]:
        sha = commit["sha"]
        author = commit["commit"]["author"]["name"]
        print(f"{sha}: {author}")
