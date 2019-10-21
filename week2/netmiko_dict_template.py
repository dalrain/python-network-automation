#!/usr/bin/env python

from getpass import getpass
from netmiko import ConnectHandler

lab_password = getpass()

devices = [
    {
    'host':'cisco3.lasthop.io',
    'username':'pyclass',
    'password':lab_password,
    'device_type':'cisco_xe',
    #'session_log':'session_log.log',
    },   
    {
    'host':'cisco4.lasthop.io',
    'username':'pyclass',
    'password':lab_password,
    'device_type':'cisco_xe',
    #'session_log':'session_log.log',
    },   
    {
    'host':'arista1.lasthop.io',
    'username':'pyclass',
    'password':lab_password,
    'device_type':'arista_eos',
    #'session_log':'session_log.log',
    },
    {
    'host':'arista2.lasthop.io',
    'username':'pyclass',
    'password':lab_password,
    'device_type':'arista_eos',
    #'session_log':'session_log.log',
    },
    {
    'host':'arista3.lasthop.io',
    'username':'pyclass',
    'password':lab_password,
    'device_type':'arista_eos',
    #'session_log':'session_log.log',
    },
    {
    'host':'arista4.lasthop.io',
    'username':'pyclass',
    'password':lab_password,
    'device_type':'arista_eos',
    #'session_log':'session_log.log',
    },
    {
    'host':'srx2.lasthop.io',
    'username':'pyclass',
    'password':lab_password,
    'device_type':'juniper',
    #'session_log':'session_log.log',
    },      
    { 
    'host':'nxos1.lasthop.io',
    'username':'pyclass',
    'password':lab_password,
    'device_type':'cisco_nxos',
    #'session_log':'session_log.log',
    },
    {
    'host':'nxos2.lasthop.io',
    'username':'pyclass',
    'password':lab_password,
    'device_type':'cisco_nxos',
    #'session_log':'session_log.log',
    },   
    ]

#BEGIN INTERACTIVE PORTION

for device in devices[7:9]:
    net_connect = ConnectHandler(**device)
    print(net_connect.find_prompt())

    
