#!/usr/bin/python3
"""test comment"""
import urllib.request


if __name__ == "main":
    req = urllib.request.Request("https://intranet.hbtn.io/status")
    with urllib.request.urlopen(req) as resp:
        body = resp.read()
        print("Body response:")
        print("type: {}".format(type(body)))
        print("content: {}".format(body))
        print("utf8 content: {}".format(body.decode("utf-8")))
