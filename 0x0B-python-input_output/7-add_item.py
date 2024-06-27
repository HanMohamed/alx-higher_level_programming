#!/usr/bin/python3
import sys

load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

filename = "add_item.json"


for i in range(1, len(sys.argv)):
#for arg in sys.argv:
    save_to_json_file(sys.argv[i], filename)
load_from_json_file(filename)
