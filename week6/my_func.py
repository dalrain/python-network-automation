#!/usr/bin/env/python

import yaml

def load_devices_from_yaml(filename="arista-devices.yml"):
    with open(filename) as f:
        return yaml.safe_load(f)

def output_printer(arp_list):
    for entry in arp_list:
        print(entry["address"] + "->" + entry["hwAddress"])
