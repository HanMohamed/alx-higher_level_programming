#!/bin/bash
#cURL only Methodx
curl -sI "$1" | grep -i OPTIONS | awk '{for (i=2; i<NF; i++) printf $i " "; print $NF}'
