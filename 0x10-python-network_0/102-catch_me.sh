#!/bin/bash
#cURL body size #curl -s 0.0.0.0:5000/catch_me -o /dev/null -w '%{http_code}'
curl -sL -X PUT -d '{You got me!}' 0.0.0.0:5000/catch_mes
