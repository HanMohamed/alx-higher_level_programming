#!/bin/bash
#Catch me if you can!
curl -s 0.0.0.0:5000/catch_me -X PUT -o /dev/null -w "You got me!" 
