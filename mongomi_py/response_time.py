#!/usr/bin/env python
#encoding: utf-8
from mongoconn import mongocheck
import time
import sys
from config_read import yconfig_read
yml_data = yconfig_read('./config.yml')
username = yml_data['userinfo']['username']
password = yml_data['userinfo']['password']
database =  yml_data['dbinfo']['database']['name']
collection = yml_data['dbinfo']['database']['collection']
try:
  mongoport = int(sys.argv[1])
except (IndexError, NameError):
  print "You need specify a port"
  sys.exit(1)
else:
  start_time = time.time()
  client,data = mongocheck('192.168.100.141',mongoport,'admin','123456',admincommand='serverStatus')
  if client:
    test_collection =  client[database][collection]
    end_time = time.time()
    result = (end_time - start_time) if test_collection.find_one() else 'mongo中没有查到数据'
    print result
  else:
    print 'mongo connection refused'
    sys.exit(1)