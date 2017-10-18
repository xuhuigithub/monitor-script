#!/usr/bin/env python
#encoding: utf-8
from elasticsearch import exceptions
from elasticsearch import Urllib3HttpConnection
# Urllib3HttpConnection.timeout = 3
try:
  respon_result = Urllib3HttpConnection(host='192.168.206.82').perform_request(method='GET',url='/',timeout=3)
  respon_code = respon_result[0]
except exceptions.ConnectionError:
  result = 'es not response'
except IndexError:
  result = 'es web response error text'
else:
  result = 'up' if respon_code == 200 else 'error %s' %respon_code
finally:
  print result