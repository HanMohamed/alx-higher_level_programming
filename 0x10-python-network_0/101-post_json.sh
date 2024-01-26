#!/bin/bash
#cURL a JSON file
curl -s "$1" -X POST -H "Content-Type: application/json" -d @"$2" DESTINATION
