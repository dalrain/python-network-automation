#!/usr/bin/env/python

from lxml import etree

with open("show_security_zones.xml", "r") as f:
    show_security_zones = etree.fromstring(f.read())

print("This is the xml variable and its type")
print(show_security_zones)
print(type(show_security_zones))
