#!/bin/bash
#cURL body size
curl -sIL "$1" -o /dev/null -w '%{http_code}\n'