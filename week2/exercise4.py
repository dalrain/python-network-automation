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


connectionHandle = ConnectHandler(**devices[0])

configToSend = ["ip name-server 1.1.1.1", "ip name-server 1.0.0.1", "ip domain-lookup"]

output = connectionHandle.send_config_set(configToSend)
print("Configuration change:")
pprint(output)

test_output = connectionHandle.send_command("ping google.com")
if "!!" in test_output:
    print("Ping test worked")
    print(test_output)
else:
    raise ValueError("Ping didn't work: {}\n\n".format(test_output))

connectionHandle.disconnect()

