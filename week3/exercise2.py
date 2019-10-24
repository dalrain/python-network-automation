#!/usr/bin/env python

from pprint import pprint
import yaml

devices = [
    {
    'host':'cisco3.lasthop.io',
    'username':'cisco_admin',
    'password':"secret",
    'device_type':'cisco_ios',
    #'session_log':'session_log.log',
    },   
    {
    'host':'cisco4.lasthop.io',
    'username':'cisco_admin',
    'password':"secret",
    'device_type':'cisco_ios',
    #'session_log':'session_log.log',
    },   
    {
    'host':'arista1.lasthop.io',
    'username':'cisco_admin',
    'password':"secret",
    'device_type':'arista_eos',
    #'session_log':'session_log.log',
    },
    {
    'host':'arista2.lasthop.io',
    'username':'cisco_admin',
    'password':"secret",
    'device_type':'arista_eos',
    #'session_log':'session_log.log',
    },
    {
    'host':'arista3.lasthop.io',
    'username':'cisco_admin',
    'password':"secret",
    'device_type':'arista_eos',
    #'session_log':'session_log.log',
    },
    {
    'host':'arista4.lasthop.io',
    'username':'cisco_admin',
    'password':"secret",
    'device_type':'arista_eos',
    #'session_log':'session_log.log',
    },
    {
    'host':'srx2.lasthop.io',
    'username':'cisco_admin',
    'password':"secret",
    'device_type':'juniper',
    #'session_log':'session_log.log',
    },      
    { 
    'host':'nxos1.lasthop.io',
    'username':'cisco_admin',
    'password':"secret",
    'device_type':'cisco_nxos',
    #'session_log':'session_log.log',
    },
    {
    'host':'nxos2.lasthop.io',
    'username':'cisco_admin',
    'password':"secret",
    'device_type':'cisco_nxos',
    #'session_log':'session_log.log',
    },   
    ]

pprint(devices)

with open("devices.yml", "w") as fileHandle:
    yaml.dump(devices, fileHandle, default_flow_style=False)
