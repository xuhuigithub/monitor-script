#!/usr/bin/env python
#encoding: utf-8
from mongoconn import mongocheck
from Calc import Rate
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
    result,data = mongocheck('192.168.100.142',mongoport,username,password,admincommand='serverStatus')
    if result:
      curconn = data['connections']['current']
      avaconn = data['connections']['available']
      # print data['mem']['resident'],'M'
      print Rate(curconn,avaconn)
    else:
      print "connection return False"
      sys.exit(1)