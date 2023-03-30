#!/bin/bash
#print body of responses greater than 200
curl -sfL "$1" -X GET
