#!/usr/bin/env/python

import devices_dict
from devices_dict import devices
from netmiko import ConnectHandler

#for device in devices[7:9]:
#    net_connect = ConnectHandler(**device)
#    print(net_connect.find_prompt())
#    net_connect.disconnect() 

connectionHandle = ConnectHandler(**devices[1])

output = connectionHandle.send_command_timing("ping", strip_prompt=False, strip_command=False)
output += connectionHandle.send_command_timing("\n", strip_prompt=False, strip_command=False)
output += connectionHandle.send_command_timing("8.8.8.8", strip_prompt=False, strip_command=False)
output += connectionHandle.send_command_timing("\n", strip_prompt=False, strip_command=False)
output += connectionHandle.send_command_timing("\n", strip_prompt=False, strip_command=False)
output += connectionHandle.send_command_timing("\n", strip_prompt=False, strip_command=False)
output += connectionHandle.send_command_timing("\n", strip_prompt=False, strip_command=False)
output += connectionHandle.send_command_timing("\n", strip_prompt=False, strip_command=False)

connectionHandle.disconnect()

print()
print(output)
print()
