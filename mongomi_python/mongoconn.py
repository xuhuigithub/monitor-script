#!/usr/bin/env python
#encoding: utf-8
try:
  # Python 3.x
  from urllib.parse import quote_plus
except ImportError:
  # Python 2.x
  from urllib import quote_plus
from pymongo.errors import ServerSelectionTimeoutError
from pymongo import MongoClient
from sys import argv
def mongocheck(host,port,user,password,admincommand='isMaster'):
  user = quote_plus(user)
  password = quote_plus(password)
  client = MongoClient('mongodb://%s:%s@%s:%s/'%(user,password,host,port),serverSelectionTimeoutMS=2)
  try:
    data = client.admin.command(admincommand)
  except ServerSelectionTimeoutError:
    return False,'server not availabe'
  else:
    return True,data
    client.close()

if __name__ == "__main__":
  try:
    port = argv[1]
  except Exception:
    print 'You need specify a port'
  else:
    result,data = mongocheck('192.168.206.47',port,'Admin','Chinadaas@2017mongo',admincommand='serverStatus')
    #admincommand:ServerStatus,isMaster
    if result:
      print 'up'
    else:
      print 'down'
