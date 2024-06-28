#!/usr/bin/python3
"""7. Load, add, save
Write a script that adds all arguments to a Python list,
and then save them to a file"""
import sys

load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

filename = "add_item.json"

try:
    loaded_obj = load_from_json_file(filename)
except:
    loaded_obj = []
    
for args in sys.argv[1:]:
    loaded_obj.append(args)

save_to_json_file(loaded_obj, filename)
