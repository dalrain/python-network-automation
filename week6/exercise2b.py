#!/usr/bin/env/python

import pyeapi
from getpass import getpass
from pprint import pprint
from my_func import load_devices_from_yaml, output_printer


device_dict = load_devices_from_yaml()
device_password = getpass()

for item, device_detail in device_dict.items():
    device_detail["password"] = device_password

    # This takes transport, host, username, password, and port
    connection = pyeapi.client.connect(**device_detail)

    #This takes an existing connection and creates a Node instance
    device = pyeapi.client.Node(connection)

    output = device.enable("show ip arp")

    output_printer(output[0]["result"]["ipV4Neighbors"])
