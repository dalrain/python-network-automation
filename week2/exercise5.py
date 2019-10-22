#!/usr/bin/env/python

import devices_dict
from devices_dict import devices
from netmiko import ConnectHandler
from datetime import datetime
from pprint import pprint

#for device in devices[7:9]:
#    net_connect = ConnectHandler(**device)
#    print(net_connect.find_prompt())
#    net_connect.disconnect() 


for device in devices[7:]:
    connectionHandle = ConnectHandler(**device)
    output = connectionHandle.send_config_from_file("vlans.txt")
    pprint(output)
    connectionHandle.save_config()
    connectionHandle.disconnect()


