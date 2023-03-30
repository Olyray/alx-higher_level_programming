#!/bin/bash
# Print the options
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
