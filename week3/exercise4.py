#!/usr/bin/env/python

import json

with open("arista.json") as fileHandle:
    test_data = json.load(fileHandle)

arp_dict = {}
arp_neighbors = test_data["ipV4Neighbors"]

for entry in arp_neighbors:
    arp_dict[entry["address"]] = entry["hwAddress"]

print(arp_dict)
