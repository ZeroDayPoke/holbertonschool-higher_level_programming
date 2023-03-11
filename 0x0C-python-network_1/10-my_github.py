#!/usr/bin/python3
"""
Write a Python script that takes your GitHub credentials
(username and password) and uses the GitHub API to display your id
"""
import requests as rq
from requests.auth import HTTPBasicAuth
import sys


if __name__ == "__main__":
    url = 'https://api.github.com/user'
    username = sys.argv[1]
    fine_token = sys.argv[2]
    req = rq.get(url, auth=HTTPBasicAuth(username, fine_token)).json()
    print(req.get('id'))
