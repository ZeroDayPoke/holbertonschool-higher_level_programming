#!/usr/bin/python3
"""
Write a Python script that takes in a letter
and sends a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter.
"""
import requests as rq
import sys


if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    if len(sys.argv) == 1:
        q = ""
    else:
        q = sys.argv[1]

    req = rq.post(url, data={"q": q})
    try:
        a_dict = req.json()
        id = a_dict.get('id')
        name = a_dict.get('name')
        if len(a_dict) == 0:
            print('No result')
        else:
            print('[{}] {}'.format(id, name))
    except Exception as e:
        print('Not a valid JSON')
