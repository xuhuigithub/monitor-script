#!/usr/bin/env python
#encoding: utf-8
import yaml
from mongoconn import mongocheck
from psutil import Process
from config_read import yconfig_read
import sys
if __name__ == "__main__":
  try:
    mongoport = int(sys.argv[1])
  except (IndexError, NameError):
    print "You need specify a port"
  else:
    yml_data = yconfig_read('./config.yml')
    username = yml_data['userinfo']['username']
    password = yml_data['userinfo']['password']
    result,data = mongocheck('192.168.100.141',mongoport,username,password,admincommand='serverStatus')
    if result:
      p = Process(data['pid'])
      rss_mem = p.memory_info().rss
      print (int(rss_mem)/1024)/1024
    else:
      print "connection return False"
      sys.exit(1)
