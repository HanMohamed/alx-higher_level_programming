#!/bin/bash
#cURL a JSON file
curl -s "$1" -X POST -H "Accept: application/json" "$2"
