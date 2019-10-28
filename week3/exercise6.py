#!/usr/bin/env/python

import yaml
from netmiko import ConnectHandler
from os import path
from ciscoconfparse import CiscoConfParse

with open(path.join(path.expanduser("~"), ".netmiko.yml")) as f:
    netmiko_yaml = yaml.load(f)

device = netmiko_yaml['cisco4']
connectionHandle = ConnectHandler(**device)
show_run_result = connectionHandle.send_command("show run")

# NB splitlines returns a list, which CiscoConfParse needs

parse_obj = CiscoConfParse(show_run_result.splitlines())
#This will use a regexp raw string to search for both parent and child, returns interfaces that also have an ip address assigned thereafter
interfaces = parse_obj.find_objects_w_child(
    parentspec=r"^interface", childspec=r"^\s+ip address"
)

for interface in interfaces:
    print("Interface: {}".format(interface.text))
    for ip_address in interface.re_search_children(r"ip address"):
        print("IP Addresses line: {}".format(ip_address.text))
    print()
