#!/usr/bin/env/python

#This is required to parse out the natively returned XML data structures from Juniper RPC calls
from lxml import etree

from jnpr.junos import Device

from jnpr_devices import srx2

from pprint import pprint

device_object = Device(**srx2)
device_object.open()


# Exercise 5a
print("Get show version output using PyEZ RPC calls")

show_version_xml = device_object.rpc.get_software_information()
pprint(etree.tostring(show_version_xml, encoding="unicode"))


# Exercise 5b

print("Show the interfaces of the device with the 'terse' keyword")
show_interfaces_terse = device_object.rpc.get_interface_information(terse=True)
pprint(etree.tostring(show_interfaces_terse, encoding="unicode"))

#Exercise 5c

print("Show the single interface fe-0/0/7 using terse, and have the XML tree object pretty print it")
show_interfaces_terse = device_object.rpc.get_interface_information(interface_name="fe-0/0/7", terse=True, normalize=True)
pprint(etree.tostring(show_interfaces_terse, pretty_print=True, encoding="unicode"))
