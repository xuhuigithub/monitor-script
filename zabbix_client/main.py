#!/usr/bin/env python
#encoding: utf-8
from config_read import yconfig_read
from Zabbix_api import Zabbix

Server = Zabbix(uri='192.168.203.91',username='admin',password='zabbix_king')
hosts = yconfig_read('./hostinfo.yml')
result = Server.createhosts(hosts=hosts)
print result