#!/usr/bin/python3
"""Uses an email variale in a POST request"""
import requests
from sys import argv


if __name__ == "__main__":
    response = requests.post(argv[1], data={"email": argv[2]})
    print(response.text)
