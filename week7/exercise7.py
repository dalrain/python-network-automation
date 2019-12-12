#!/usr/bin/env/python

import os
from getpass import getpass

from nxapi_plumbing import Device

from lxml import etree

#This import is required just to override certificate issues with self signed certs

import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

#This sets the variable to actually disable warnings in the library
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

password = getpass()

device = Device(
    api_format="xml",
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

# Use the data vars returned from the show command, they will be XML because we used that api_format
print("Interface: {interface} State: {state} and MTU {eth_mtu}".format(
    interface=interface_output.find(".//interface").text,
    state=interface_output.find(".//state").text,
    eth_mtu=interface_output.find(".//eth_mtu").text,
    )
)

# Exercise 7b

print("Run multiple show commands, show system uptime and show system resources")
multi_show_output = device.show_list(["show system uptime", "show system resources"])
for output in multi_show_output:
    print(etree.tostring(output, encoding="unicode"))

# Exercise 7c

print("make config changes, add loopbacks with descriptions")

commands = [
    "interface loopback141",
    "description loopback141",
    "no shutdown",
    "interface loopback142",
    "description loopback142",
    "no shutdown",
]

output = device.config_list(commands)

# The output will be a list of all the command results, so we'll read them one at a time

for returned in output:
    print(etree.tostring(returned, encoding="unicode"))
