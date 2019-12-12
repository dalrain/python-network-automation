#!/usr/bin/env/python

import os
from getpass import getpass

from nxapi_plumbing import Device

#This import is required just to override certificate issues with self signed certs

import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

#This sets the variable to actually disable warnings in the library
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

password = getpass()

device = Device(
    api_format="jsonrpc",
    host="nxos1.lasthop.io",
    username="pyclass",
    password=password,
    transport="https",
    port=8443,
    verify=False,
)

print("Pull in the interface 1/1 info:")

# .show will allow us to pull read data from the device
interface_output = device.show("show interface Ethernet1/1")
interface_output = interface_output["TABLE_interface"]["ROW_interface"]

# Use the raw data vars returned from the show command, they will be more like dicts because we used JSON
print("Interface: {interface} State: {state} and MTU {eth_mtu}".format(**interface_output))
