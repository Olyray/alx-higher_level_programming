#!/usr/bin/python3
"""Uses an email variale in a POST request"""
import sys
import requests


if __name__ == "__main__":
    website = sys.argv[1]
    address = {"email": sys.argv[2]}

    r = requests.post(website, data=address)
    print(r.text)
