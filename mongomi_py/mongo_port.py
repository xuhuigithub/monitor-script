#!/usr/bin/env python
#encoding: utf-8
import json
import sys
try:
  port_file = sys.argv[1]
except (IndexError, NameError):
  print "You need specify a file"
else:
  with open('./mongod.port','r') as f:
    data =  f.read().strip().split()
  json_data = {'data':[]}
  for i in data:
    dict_content = {"{#MONGO_PORT}" : i}
    json_data['data'].append(dict_content)
  print json.dumps(json_data,sort_keys=True,indent=4)

