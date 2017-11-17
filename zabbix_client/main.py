#!/usr/bin/env python
#encoding: utf-8
from config_read import yconfig_read
from Zabbix_api import Zabbix

if __name__ == "__main__":
  Server = Zabbix(uri='192.168.203.91',username='admin',password='zabbix_king')
  hosts = yconfig_read('./hostinfo.yml')
  result = Server.createhosts(hosts=hosts)
  for i in result:
    print i
  # media_data = {
  #   "jsonrpc": "2.0",
  #   "method": "user.create",
  #   "params": {
  #       "alias": "宫新胜",
  #       "passwd": "Chinadaas@2017",
  #       "usrgrps": [
  #         {
  #           "usrgrpid": "26",
  #         }
  #       ],
  #       "user_medias":[
  #         {
  #           "mediatypeid" : "5",
  #           "sendto": "gongxinsheng@chinadaas.com",
  #           "active": 0,
  #           "severity": 63,
  #           "period": "1-7,00:00-24:00",
  #         },
  #         {
  #           "mediatypeid": "6",
  #           "sendto": "18610811144",
  #           "active": 0,
  #           "severity": 63,
  #           "period": "1-7,00:00-24:00",
  #         }
  #       ],
  #   },
  # }
  # data = {
  #   "jsonrpc": "2.0",
  #   "method": "mediatype.get",
  #   "params": {
  #     "output": "extend"
  #   },
  # }
  # result = Server.commongateway(media_data)
  # print result