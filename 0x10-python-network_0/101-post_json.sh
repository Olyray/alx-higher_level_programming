#!/bin/bash
# Pass in a JSON along with a POST request
curl -s -X POST -H "Content-Type: application/json" -d @$2 $1
