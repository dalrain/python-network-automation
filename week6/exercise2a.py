#!/usr/bin/env/python

import pyeapi
import yaml
from getpass import getpass
from pprint import pprint

def load_devices_from_yaml(filename="arista-devices.yml"):
    with open(filename) as f:
        return yaml.safe_load(f)

device_dict = load_devices_from_yaml()
device_password = getpass()

for item, device_detail in device_dict.items():
    device_detail["password"] = device_password

    # This takes transport, host, username, password, and port
    connection = pyeapi.client.connect(**device_detail)

    #This takes an existing connection and creates a Node instance
    device = pyeapi.client.Node(connection)

    output = device.enable("show ip arp")

    for entry in output[0]["result"]["ipV4Neighbors"]:
        print(entry["address"] + "->" + entry["hwAddress"])

