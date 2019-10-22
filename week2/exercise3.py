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


connectionHandle = ConnectHandler(**devices[1])

commands = ["show version", "show lldp neighbors"]

for command in commands:
    output = connectionHandle.send_command(command, use_textfsm=True)
    print(command)
    pprint(output)

    if command == "show version":
        print("The version response is of type {}".format(type(output)))

    if command == "show lldp neighbors":
        print("The LLDP response is a {}".format(type(output)))
        print("The HPE switch connection port is: {}".format(output[0]["neighbor_interface"]))

connectionHandle.disconnect()

