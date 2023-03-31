#!/usr/bin/python3
"""Python module to check for a valid JSON"""
import requests
from sys import argv
import json


if __name__ == "__main__":
    breakpoint()
    if len(argv) == 1:
        letter = {"q": ""}
    else:
        letter = {"q": argv[1]}
    response = requests.post("http://0.0.0.0:5000/search_user", data=letter)
    try:
        data = response.json()
        if data == {}:
            print("No result")
        else:
            print("[{}] {}".format(data.get("id"), data.get("name")))
    except ValueError:
        print("Not a valid JSON")
