#!/usr/bin/env/python

import devices_dict
from devices_dict import devices
from devices_dict import lab_password
from netmiko import ConnectHandler
from datetime import datetime
from pprint import pprint
import time

#for device in devices[7:9]:
#    net_connect = ConnectHandler(**device)
#    print(net_connect.find_prompt())
#    net_connect.disconnect() 

devices[1]["secret"] = lab_password
devices[1]["session_log"] = "my_output.txt"

connectionHandle = ConnectHandler(**devices[1])

print("\nThe current prompt appears to be:"+connectionHandle.find_prompt())

print("\nNow entering config mode, prompt appears to be:")
connectionHandle.config_mode()
print(connectionHandle.find_prompt())

print("\nExiting config mode, prompt now:")
connectionHandle.exit_config_mode()
print(connectionHandle.find_prompt())

print("\nExit privileged exec mode, prompt now:")
connectionHandle.write_channel("disable\n")
time.sleep(2)
print(connectionHandle.read_channel())

print("\nBack to enable mode, prompt now:")
connectionHandle.enable()
print(connectionHandle.find_prompt())

connectionHandle.disconnect()

