#!/usr/bin/env python

from getpass import getpass
from netmiko import ConnectHandler

net_connect = ConnectHandler(
    host='nxos1.lasthop.io',
    username='pyclass',
    password=getpass(),
    device_type='cisco_nxos',
    session_log='session_log.log')
print(net_connect.find_prompt())
