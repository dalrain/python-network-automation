#!/usr/bin/env/python

import yaml
from pprint import pprint
from os import path
from netmiko import ConnectHandler

filename = path.join(path.expanduser("~"), ".netmiko.yml")

with open(filename) as f:
    netmiko_yaml = yaml.load(f)

connectionHandle = ConnectHandler(**netmiko_yaml["cisco3"])

print(connectionHandle.find_prompt())
