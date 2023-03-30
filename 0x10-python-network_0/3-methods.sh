#!/bin/bash
# Print the options
curl -sI "$1" | awk '/Allow/ {gsub(",", ", "); print substr($0, index($0, $2))}'
