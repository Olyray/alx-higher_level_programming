#!/usr/bin/python3
"""A script to fill a json file"""

import sys
import json
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file


try:
    my_list = load_from_json_file("add_item.json")
except (FileNotFoundError, json.decoder.JSONDecodeError):
    my_list = []

for i in range(1, len(sys.argv)):
    my_list.append(sys.argv[i])

save_to_json_file(my_list, "add_item.json")
