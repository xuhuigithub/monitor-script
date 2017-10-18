#!/usr/bin/env python
#encoding: utf-8
import requests
import json
class Zabbix(object):
  def __init__(self,uri,username,password):
    self.__username = username
    self.__passwrod = password
    self.uri = uri
    headers = {'content-type': 'application/json'}
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
    res = requests.post('http://%s/api_jsonrpc.php'%self.uri, data=json.dumps(data), headers=headers)
    self.token = res.json().get('result')

  def getgroups(self):
    headers = {'content-type': 'application/json'}
    data = {
      "jsonrpc": "2.0",
      "method": "hostgroup.get",
      "params": {
        "output": "extend",
      },
      "auth": self.token,
      "id": 1
    }
    res = requests.post('http://%s/api_jsonrpc.php' % self.uri, data=json.dumps(data), headers=headers)
    return res.json().get('result')
  def createhosts(self,hosts):
    result = []
    headers = {'content-type': 'application/json'}
    for host in hosts.keys():
      print host
      print hosts[host]
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
            "groups": hosts[host].get('groups')
        },
        "auth": self.token,
        "id": 1
        }
      res = requests.post('http://%s/api_jsonrpc.php' % self.uri, data=json.dumps(data), headers=headers)
      result.append(res.json())
    return result

if __name__ == "__main__":
  Server = Zabbix(uri='192.168.203.91',username='admin',password='zabbix_king')
  groupids = Server.getgroups()
  try:
    for i in groupids:
      result = "groupname: %s" %(i['name']),"groupid: %s"%(i['groupid'])
      print result
  except KeyError:
    print '返回的结果不对！',groupids