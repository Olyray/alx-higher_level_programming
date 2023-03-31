#!/usr/bin/python3
"""Fecth a URL"""
if __name__ == "__main__":
    from urllib import request

    with request.urlopen("https://alx-intranet.hbtn.io/status") as status:
        status_content = status.read()
        print("Body response:")
        print("\t- type: {}".format(type(status_content)))
        print("\t- content: {}".format(status_content))
        print("\t- utf8 content: {}".format(status_content.decode("utf-8")))
