#!/usr/bin/env/python

from getpass import getpass
from pprint import pprint

from jnpr.junos import Device

device_object = Device(host="srx2.lasthop.io", user="pyclass", password=getpass())

device_object.open()

print("Get the device facts")

pprint(device_object.facts)

print("Now get just the hostname from the facts")
# This uses a dict-like access
pprint(device_object.facts["hostname"])
