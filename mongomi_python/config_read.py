# !/usr/bin/env python
# encoding: utf-8
import yaml
def yconfig_read(configfile):
  with open(configfile,'r') as f:
    yml_data = yaml.load(f)
    return yml_data


if __name__ == "__main__":
  yml_data = yconfig_read('./config.yml')
  username = yml_data['userinfo']['username']
  password = yml_data['userinfo']['password']
  print username, password
