#!/usr/bin/env/python

import pyeapi
from getpass import getpass
from pprint import pprint

# This takes transport, host, username, password, and port
connection = pyeapi.client.connect(
    transport="https",
    host="arista4.lasthop.io",
    username = "pyclass",
    password = getpass(),
    port = "443",
)
#This takes an existing connection and creates a Node instance
device = pyeapi.client.Node(connection)

output = device.enable("show ip arp")

for entry in output[0]["result"]["ipV4Neighbors"]:
    print(entry["address"] + "->" + entry["hwAddress"])

