# !/usr/bin/env python
# encoding: utf-8
import sys
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
try:
  mongoport = int(sys.argv[1])
except (IndexError,NameError):
  print "You need specify a port"
else:
  try:
    conn = MongoClient('localhost',mongoport,connectTimeoutMS=2)
  except ConnectionFailure:
    print "mongoprot %s can't be connection" %(mongoport)
  else:
    print "up"
    conn.close()
