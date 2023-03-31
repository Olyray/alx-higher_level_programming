#!/bin/bash
# Print the size of the response
curl -s -o /dev/null -w '%{size_download}\n' $1 
