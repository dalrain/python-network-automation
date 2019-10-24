#!/usr/bin/env/python

import json

with open("nxos_unit_test.json") as fileHandle:
    test_data = json.load(fileHandle)

ipv4_list = []
ipv6_list = []

for interface, ipaddr_dict in test_data.items():
    for protocol, addr_info in ipaddr_dict.items():
        for ip_address, prefix_dict in addr_info.items():
            prefix = prefix_dict["prefix_length"]
            if protocol == "ipv4":
                ipv4_list.append(str(ip_address) + "/" + str(prefix))
            elif protocol == "ipv6":
                ipv6_list.append(str(ip_address) + "/" + str(prefix))

print(ipv4_list)
print(ipv6_list)
