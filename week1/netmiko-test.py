#!/usr/bin/env/python

from getpass import getpass
from netmiko import ConnectHandler

lab_password = getpass()

devices = [{ 
    'host':'nxos1.lasthop.io',
    'username':'pyclass',
    'password':lab_password,
    'device_type':'cisco_nxos',
    'session_log':'session_log.log'},
    {
    'host':'nxos2.lasthop.io',
    'username':'pyclass',
    'password':lab_password,
    'device_type':'cisco_nxos',
    'session_log':'session_log.log'},    
    ]

for device in devices:
    net_connect = ConnectHandler(**device)
    print(net_connect.find_prompt())
    output = net_connect.send_command("show ip int bri vrf all")
    print(output)

with open("show_version.log","w") as f:
    f.writelines(net_connect.send_command("show version"))
    
