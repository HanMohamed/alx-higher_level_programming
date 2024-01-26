#!/bin/bash
#cURL body size #curl -s 0.0.0.0:5000/catch_me -o /dev/null -w '%{http_code}'
curl -s 0.0.0.0:5000/catch_me -X PUT -o /dev/null -w "You got me!" 