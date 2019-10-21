#!/usr/bin/env/python

import devices_dict
from devices_dict import devices
from netmiko import ConnectHandler

for device in devices[7:9]:
    net_connect = ConnectHandler(**device)
    print(net_connect.find_prompt())
    net_connect.disconnect() 
