#!/usr/bin/env/python

import devices_dict
from devices_dict import devices
from netmiko import ConnectHandler

#for device in devices[7:9]:
#    net_connect = ConnectHandler(**device)
#    print(net_connect.find_prompt())
#    net_connect.disconnect() 

connectionHandle = ConnectHandler(**devices[1])

output = connectionHandle.send_command("ping", expect_string=r"Protocol", strip_prompt=False, strip_command=False)
output += connectionHandle.send_command("\n", expect_string=r"Target", strip_prompt=False, strip_command=False)
output += connectionHandle.send_command("8.8.8.8", expect_string=r"Repeat", strip_prompt=False, strip_command=False)
output += connectionHandle.send_command("\n", expect_string=r"Datagram", strip_prompt=False, strip_command=False)
output += connectionHandle.send_command("\n", expect_string=r"Timeout", strip_prompt=False, strip_command=False)
output += connectionHandle.send_command("\n", expect_string=r"Extended", strip_prompt=False, strip_command=False)
output += connectionHandle.send_command("\n", expect_string=r"Sweep", strip_prompt=False, strip_command=False)
output += connectionHandle.send_command("\n", expect_string=r"#", strip_prompt=False, strip_command=False)

connectionHandle.disconnect()

print()
print(output)
print()
