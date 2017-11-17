#!/usr/bin/env python
#encoding: utf-8
import requests
import json
import re
class Zabbix(object):
  def __init__(self,uri,username,password):
    self.__username = username
    self.__passwrod = password
    self.uri = uri
    self.headers = {'content-type': 'application/json'}
    data = {
      "jsonrpc": "2.0",
      "id": 1,
      "method": "user.login",
      "params": {
        "user": self.__username,
        "password": self.__passwrod,
      },
      "auth": None,
    }
    res = requests.post('http://%s/api_jsonrpc.php'%self.uri, data=json.dumps(data), headers=self.headers)
    self.token = res.json().get('result')

  @property
  def getgroups(self):
    data = {
      "jsonrpc": "2.0",
      "method": "hostgroup.get",
      "params": {
        "output": ['groupid','name'],
      },
      "auth": self.token,
      "id": 1
    }
    res = requests.post('http://%s/api_jsonrpc.php' % self.uri, data=json.dumps(data), headers=self.headers)
    return res.json().get('result')

  @property
  def gettemplates(self):
    data = {
      "jsonrpc": "2.0",
      "method": "template.get",
      "params": {
        "output": ['templateid','name'],
      },
      "auth": self.token,
      "id": 1
    }
    res = requests.post('http://%s/api_jsonrpc.php' % self.uri, data=json.dumps(data), headers=self.headers)
    return res.json().get('result')

  def commongateway(self,data):
    data = data
    data['auth'] = self.token
    data['id'] = 1
    res = requests.post('http://%s/api_jsonrpc.php' % self.uri, data=json.dumps(data), headers=self.headers)
    print res.json()
    return res.json().get('result')

  def createhosts(self,hosts):
    result = []
    for host in hosts.keys():
      data = {
        "jsonrpc": "2.0",
        "method": "host.create",
        "params": {
            "host": host,
            "interfaces": [
                {
                    "type": 1,
                    "main": 1,
                    "useip": 1,
                    "ip": hosts[host].get('ip'),
                    "dns": "",
                    "port": hosts[host].get('port')
                }
            ],
            "groups": hosts[host].get('groups'),
            "templates": hosts[host].get('templates')
        },
        "auth": self.token,
        "id": 1
        }
      res = requests.post('http://%s/api_jsonrpc.php' % self.uri, data=json.dumps(data), headers=self.headers)
      result.append(res.json())
    return result

if __name__ == "__main__":
  Server = Zabbix(uri='192.168.203.91',username='admin',password='zabbix_king')
  groupids = Server.getgroups
  templateids = Server.gettemplates
  try:
    for i in groupids:
      if re.search('4.0',str(i)):
        print i
    for z in templateids:
      if re.search('Partition check',str(z)):
        print z
  except KeyError:
    print '返回的结果不对！',groupids