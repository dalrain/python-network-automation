#!/usr/bin/env/python

import devices_dict
from devices_dict import devices
from netmiko import ConnectHandler
from datetime import datetime

#for device in devices[7:9]:
#    net_connect = ConnectHandler(**device)
#    print(net_connect.find_prompt())
#    net_connect.disconnect() 

command = "show lldp neighbors detail"

devices[-1]["global_delay_factor"] = 2
connectionHandle = ConnectHandler(**devices[-1])

start_time = datetime.now()
output = connectionHandle.send_command(command)
end_time = datetime.now()

print(output)
print("\n\nRun time was : {}".format(end_time-start_time))

start_time = datetime.now()
output = connectionHandle.send_command(command, delay_factor=8)
end_time = datetime.now()

print(output)
print("\n\nRun time was : {}".format(end_time-start_time))

connectionHandle.disconnect()

