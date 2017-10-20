#!/usr/bin/env python
#encoding: utf-8
from elasticsearch import exceptions
from elasticsearch import Urllib3HttpConnection
# Urllib3HttpConnection.timeout = 3
import argparse
parser = argparse.ArgumentParser(description="Request Elasticsearch API")
parser.add_argument('-p','--port',type=int,required=True,help='specify a web port')
args = parser.parse_args()
port = args.port
try:
  respon_result = Urllib3HttpConnection(host='192.168.206.82',port=port).perform_request(method='GET',url='/',timeout=3)
  respon_code = respon_result[0]
except exceptions.ConnectionError:
  result = 'es not response'
except IndexError:
  result = 'es web response error text'
else:
  result = 'up' if respon_code == 200 else 'error %s' %respon_code
finally:
  print result